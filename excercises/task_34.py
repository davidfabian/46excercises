__author__ = 'd'

'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
 language, the works of an author, or in a single text. Define a function that given the file name of a text will
 return all its hapaxes. Make sure your program ignores capitalization.
'''
'''
test file location:
D:\python\46excercises\data\wordcount.txt
'''

import re


def hapax(location):
    f = open(location, 'r')
    h_count = 0
    freq = {}
    for line in f:
        word = re.split('\W+', line)
        for each in word:
            if re.match('\w+', each):

                if each.lower() in freq:
                    freq[each.lower()] += 1
                else:
                    freq[each.lower()] = 1
    for i in freq:
        if freq[i] == 1:
            h_count += 1
            print(i)
    print(len(freq), 'words found.', h_count, 'hapaxes')
    print(freq)
    f.close()

filename = input('path and filename: ')
hapax(filename)
# hapax('D:/python/46excercises/data/wordcount.txt')