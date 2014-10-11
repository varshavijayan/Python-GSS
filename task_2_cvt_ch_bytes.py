# -*- coding: utf-8 -*-
"""
Created on Thu Oct 09 19:01:40 2014

@author: Varsha
"""

import os
import binascii

def cls():
    os.system(['clear','cls'][os.name == 'nt'])
cls()

# read from file
f = open('task_1_test.txt', 'r')
print f.read() # print the sentence

#Q1 - how to identify encoding of string in file?

scale = 16 ## equals to hexadecimal
num_of_bits = 8

# loop character-by-character
with open('task_1_test.txt') as f:
    print "Character-by-character:"
    for line in f:
        for c in line:
            temp = bin(int(binascii.hexlify(c), 16))
            #binary_string = binascii.unhexlify(temp) # unhexlify works for even string lengths only
            binary_string = bin(int(temp, scale))[2:].zfill(num_of_bits)
            print c, binary_string # printing character & binary representation
            

            
            
            
            