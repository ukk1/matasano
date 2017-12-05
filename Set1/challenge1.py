#!/usr/bin/python

#Convert hex to base64

import base64
import binascii

#First we convert the hex string to bytes and then we convert the string to base64
encode = binascii.unhexlify('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d').encode('base64')
print encode