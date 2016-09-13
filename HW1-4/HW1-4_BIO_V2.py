#!/usr/bin/env python

import os, sys, re
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def main():
	# get input sequence
	dna_seq = raw_input('Type your DNA sequence: ')
	
	# Seq object call
	dna_seq = Seq(dna_seq, generic_dna)
	
	# call reverse_complement function in Bio.Seq
	dna_seq = dna_seq.reverse_complement()
	
	# print output
	print "Reverse complement DNA: ", dna_seq
	
	# exit program
	sys.exit()
	
if __name__ == '__main__':
	main()
