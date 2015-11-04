__author__ = 'd'
'''
Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file).
'''
'''
D:\python\46excercises\data\palindrome.txt
'''


import os
import re

def numberlines(wo_numbers):
    f = open(wo_numbers, 'r')
    newpath = (os.path.split(wo_numbers))
    print(newpath[1])
    # newfile = re.sub('.(\.txt|\.TXT)', 'X.', newpath[1])
    print(newfile)
    #for line in f:

    f.close()


numberlines('D:/python/46excercises/data/palindrome.txt')