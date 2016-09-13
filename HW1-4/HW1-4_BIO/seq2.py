#!/usr/bin/env python

# import Biopython
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

# Ask user for input file
uf = raw_input("Please input sequence filename: \n")

# open and read the file, saving the sequence
f = open(uf, 'r')
s = f.read()

# Save the sequence as a Biopython sequence
dna = Seq(s, generic_dna)

rcs = dna.reverse_complement()

print rcs

l = len(rcs)

output = open('rcs.txt', 'w')

for i in range(1, l):
	output.write(rcs[i])

output.close()

print "Done converting.\nSee rcs.txt for output."
