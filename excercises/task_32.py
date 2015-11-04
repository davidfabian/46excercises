__author__ = 'd'
'''
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a
frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character
frequency table to the screen.
'''
'''
D:\python\46excercises\data\palindrome.txt
'''

import re


def char_freq_table(location):
    f = open(location, 'r')
    freq = {}
    for line in f:
        for i in line:
            if re.search('\w', i):
                if i in freq.keys():
                    freq[i] += 1
                else:
                    freq[i] = 1
    z = []
    z += freq.keys()
    z.sort()
    for i in z:
        print(i, end='=')
        print(freq[i] * '*')
    # print(freq)
    f.close()

filename = input('path and filename: ')
char_freq_table(filename)