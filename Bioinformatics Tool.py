"""
@Author: Chase Labbe
Purpose of this code is to develop a Bioinformatics module that will
allow the creation of tools to be used in later programs such as
Generating random sequences, turning sequences into string, finding
complementary sequences and locating start/stop codons
"""
#---------Imports-----------------------------------------
import sys, re, numpy as np
#---------Methods-----------------------------------------
def make_sequence(length, GC_Content = 1, GC_Skew = 0, AT_Skew = 0):
    """
    Generates a random DNA Sequence
    """
    nucleotides = ['A','T','G','C'] ##List of nucleotides
    probability = gen_probability (GC_Content, GC_Skew, AT_Skew ) ##Calls the probability method

    return np.random.choice( nucleotides, length, probability)
def gen_probability (GC_Content, GC_Skew = 0, AT_Skew = 0):
    """
    Calculates the GC Content, Skew, and AT, Skew
    Equations found online
    """
    G = (GC_Content*(1-((1-GC_Skew)/2)))
    C = (GC_Content - G)
    A = ((1-GC_Content) * (1-((1-AT_Skew)/2)))
    T = ( 1 - G - C- A)

    GC_Content = ((G+C)/(G+C+T+A))
    GC_Skew = ((G-C)/(G+C))
    AT_Skew = ((A-T)/(A+T))

    return [A,T,G,C]
def sequence_to_string (sequence):
    """
    Changes an array to a string
    :param sequence: Inputed sequence
    :return: String
    """
    string1 = "" ##Create an empty string

    for i in sequence:
        string1 = string1 + i ##Iterates through the sequence, adds each index to string

    return string1
def string_to_sequence (given_string):
    """
    Changes a string into an array
    :param given_string: String inputed
    :return: Array
    """
    given_string = given_string.split(',')

    return given_string
def reverse_sequence(sequence):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} ##Dictionary of base-pair complements

    reverse = ''.join([complement[key] for key in reversed (sequence)]) ##reverses the sequence
    return reverse


def find_start_codon(sequence):
    """
    Finds the start codon
    :param sequence: Input sequence
    :return: List of Start codon locations
    """
    start_codon = []  ##Empty list initialized
    orf = 0  ##Variable orf set to 0

    for i in sequence:
        if "ATG" == sequence[orf:orf + 3]:  ##If string matches sequence in triples
            start_codon.append(orf)  ##Append it to the empty list
        orf += 1
    return start_codon  ##Return list with start codon locations


def find_stop_codon(sequence):
    """
    Finds the stop codon
    :param sequence: Input sequence
    :return: List of Stop Codon locations
    """
    stop_codon = []  ##Empty list intialized
    orf = 0  ##Variable orf set to 0
    stop = "TAA", "TGA", "TAG"
    for i in sequence:
        if sequence [orf:orf + 3] in stop:  ##Searches for stop codon
            stop_codon.append(orf)  ##Adds them to the list
        orf += 1
    return stop_codon  ##Returns list with stop codon locations
##---------------Method Testing---------------------------------------------------------
##------------Genetic Probability Test--------------------------------------------------
print ("Probabilities: ", gen_probability(GC_Content=3, GC_Skew=2, AT_Skew= 4))
##------------Randomized Sequence Test--------------------------------------------------
print ("Generated Sequence: ", make_sequence(100, GC_Content=2, GC_Skew= 4, AT_Skew= 3))
##------------Sequence to String Test---------------------------------------------------
print ("Sequence to string: ", sequence_to_string("ATGTAATGATGCCG"))
##------------String to Sequence Test---------------------------------------------------
print ("String to Sequence: ", string_to_sequence("ATGTAATGTTGCCAA"))
##------------Reverse Sequence Test-----------------------------------------------------
print ("Reverse Compliment: ", reverse_sequence("TAATAGTA"))
##------------Find Start Codon Test-----------------------------------------------------
print ("Start Codon(s): ", find_start_codon("TTATATGCCGA"))
##------------Find Stop Codon Test------------------------------------------------------
print ("Stop Codon(s): ", find_stop_codon("TAATAATAATGTA"))