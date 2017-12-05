#!/usr/bin/python

#Implement repeating-key XOR

import binascii
from itertools import cycle, izip

message = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'

def repeating_xor():
	xor = ''.join(chr(ord(a) ^ ord(k)) for a,k in izip(message, cycle(key)))
	print binascii.hexlify(xor)

if __name__ == '__main__':
	repeating_xor()
