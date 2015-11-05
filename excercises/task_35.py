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
    linecount = 1
    # opens original file for reading
    f = open(wo_numbers, 'r')

    # creates new filename based on the original. first splits the filename from the path,
    # then creates new filename by adding _new to the end of original .txt file
    newpath = (os.path.split(wo_numbers))
    newpath = (os.path.join(newpath[0], re.sub('.(?=txt)', '_new.', newpath[1])))

    # creates a file with new filename
    g = open(newpath, 'w')
    for line in f:
        g.write(str(linecount) + ' ' + line)
        linecount += 1

    g.close()

    f.close()


# numberlines('D:/python/46excercises/data/palindrome.txt')