#!/usr/bin/python

#Detect single-character XOR

import re
import binascii

def evaluate(xor,count):
	etaoin = ["e","t","a","o","i","n"," ","s","h","r","d","l","u"]

	#Check how many times the ETAOIN characters appear in each of the decrypted strings
	for letter in xor:
		if letter in etaoin:
			count += 1
	print str(count) + " points for: " + xor

def xor(decoded,chars):
	for key in chars:
		count = 0
		hx = hex(ord(key))
		#Loop over the values to find the key
		xor = ''.join(chr(ord(a) ^ int(hx,16)) for a in decoded)

		evaluate(xor,count)

def main():
	chars = "1234567890abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUXYZ'\n "
	file = open('challenge4.txt')
	
	for line in file.readlines():
		line = line.strip('\n')
		decoded = binascii.unhexlify(line)
		
		xor(decoded,chars)

if __name__ == '__main__':
	main()
