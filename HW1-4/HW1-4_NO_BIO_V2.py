#!/usr/bin/env python

import os, sys, re

def reverse(s):
	"""Return the sequence string in reverse order."""
	# make a list of letters from string
	length = len(s)
	seq = [''] * (length - 2)
	o = ''
	for i in s:
		seq.append(i)

	# reverse the list
	seq.reverse()
	
	# join the letters of the list into string and return
	o = ''.join(seq)
	
	return o

def complement(s):
	"""Return the complementary sequence string."""
	# dictionary setup for complement
	base_complementary = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	
	# make a list of letters from string
	l = len(s)
	seq = []
	o = ''
	
	for i in s:
		seq.append(i)
	
	# for loop of the letters and call the base_complementary dictionary
	for i in range(0, l, 1):
		if s[i] == 'A':
			seq[i] = base_complementary['A']
		elif s[i] == 'T':
			seq[i] = base_complementary['T']
		elif s[i] == 'C':
			seq[i] = base_complementary['C']
		else:
			seq[i] = base_complementary['G']
			 
	# join the letters of the list into string and return
	o = ''.join(seq)
		
	return o

def main():
	# get input sequence
	dna_seq = raw_input('Type your DNA sequence : ')
		
	# check DNA letter (only ACGTacgt)
	for i in dna_seq: 
		if i not in 'ATCGatcg':
			print "** Error:  Not a DNA sequence"
			sys.exit()
			
	# change it to upper case
	dna_seq = dna_seq.upper()
		
	# call reverse function
	dna_seq = reverse(dna_seq)
	
	# call complement function
	dna_seq = complement(dna_seq)
	
	# print output
	print "Reverse complement DNA :", dna_seq
	
	# exit the program
	sys.exit()

if __name__ == '__main__':
	main()
