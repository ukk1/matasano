#!/usr/bin/python

#Fixed XOR

def xor():
	b1 = "1c0111001f010100061a024b53535009181c"
	b2 = "686974207468652062756c6c277320657965"

	#XOR the two values
	xor = (int(b1,16) ^ int(b2, 16))

	#Print the result in HEX-format
	print "%x" % xor

if __name__ == '__main__':
	xor()
