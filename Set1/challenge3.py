#!/usr/bin/python

#Single-byte XOR cipher

import binascii
import re

encoded = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUXYZ"

def evaluate(xor,count):
	etaoin = ["e","t","a","o","i","n"," ","s","h","r","d","l","u"]

	#Check how many times the ETAOIN characters appear in each of the decrypted strings
	for letter in xor:
		if letter in etaoin:
			count += 1
	print str(count) + " points for: " + xor

def xor():
	for key in chars:
		count = 0
		hx = hex(ord(key))
		#Loop over the values to find the key
		xor = ''.join(chr(ord(a) ^ int(hx,16)) for a in encoded)
		evaluate(xor,count)

if __name__ == '__main__':
	xor()
