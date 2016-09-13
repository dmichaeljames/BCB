#!/usr/bin/env python

# Ask user for sequence input file
uf = raw_input("Please input the name of the sequence file: \n")

# Opening the sequence file
f = open(uf,"r")

# Obtaining the sequence and closing the file
s = f.readline()
f.close()

# Determining the length of the sequence
l = len(s)

# opening the output file
rcs = open('rcs.txt','w')

# finding the base complement, starting at the end, and writing it to 
# the output file.
for i in range((l - 2), -1, -1):
	if s[i] == 'A':
		rcs.write("T")
	elif s[i] == 'T':
		rcs.write("A")
	elif s[i] == 'C':
		rcs.write("G")
	elif s[i] == 'G':
		rcs.write("C")
	else:
		print "Not a valid base."
				
# Closing the output file and finishing up.		
rcs.close()
print "Done converting.\nSee rcs.txt for output."
