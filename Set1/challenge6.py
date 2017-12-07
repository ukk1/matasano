#!/usr/bin/python

#Break repeating-key XOR
#TODO: everything else except calculating the Hamming distance

import binascii

#convert strings to binary
s1 = bin(int(binascii.hexlify("this is a test"),16))
s2 = bin(int(binascii.hexlify("wokka wokka!!!"),16))

#function that calculates the Hamming distance between two strings
def hamming(s1, s2):	
	if len(s1) != len(s2):
		print "Strings are not equal in length"
	else:
		return sum(el1 != el2 for el1, el2 in zip(s1, s2))

def main():
	file = open('challenge6.txt')

	for line in file.readlines():
		line = line.strip('\n')
		decoded = binascii.a2b_base64(line)
		print decoded

		hamming(s1,s2)

if __name__ == "__main__":
	main()