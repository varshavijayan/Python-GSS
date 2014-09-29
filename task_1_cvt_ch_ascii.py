# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 09:06:22 2014

@author: Varsha
"""

import os
def cls():
    os.system(['clear','cls'][os.name == 'nt'])
cls()


# read from file
f = open('task_1_test.txt', 'r')
print f.read() # print the sentence

# loop character-by-character
with open('task_1_test.txt') as f:
    print "Character-by-character:"
    for line in f:
        for c in line:
            # print character and corresponding ASCII code
            print c, ord(c)
