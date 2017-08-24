"""
Opens a fasta file and parses through it
"""
##---------Imports----------------------
import sys
import re
##---------Methods----------------------
def create_contigs (filename):
    file = open(filename, "r")
    header = ""
    contigs = {}

    for i in file:
        if i[0] == ">":
            header = i
            contigs[header] = ""
            continue

        contigs[header] += i

    file.close()
    return contigs
