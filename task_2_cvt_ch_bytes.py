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

# loop character-by-character
with open('task_1_test.txt') as f:
    print "Character-by-character:"
    for line in f:
        for c in line:
            temp = bin(int(binascii.hexlify(c), 16))
            print c, temp # printing character & hex representation
            
            
            
# ALL TRIALS
#import array
#import pip
#import logging
            #temp2=bytearray.fromhex(temp)
            #temp2=binascii.unhexlify(temp)
            # detect encoding
#            def force_decode(c, codecs=['utf8', 'cp1252']):
#                for i in codecs:
#                    try:
#                        return string.decode(i)
#                        print c, string.decode(i)
#                    except:
#                        pass
#
#                logging.warn("cannot decode url %s" % ([c]))

            #print c, bin(int(binascii.hexlify(c), 16)) # prints hexadecimal representation
            #temp = bin(int(binascii.hexlify(c), 16))
            #print array.array('B',c)
            #print map(ord,c)
            #print bytearray(c)
            #print temp
            #byte_list = map(ord, temp)
            #print c, byte_list
            #print bytearray.fromhex(temp)
            
            
            
            