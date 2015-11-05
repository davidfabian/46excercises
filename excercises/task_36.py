__author__ = 'd'
'''
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the
lengths of the word tokens in the text, divided by the number of word tokens).
'''
'''
D:/python/46excercises/data/palindrome.txt
'''


def word_average(a):

    word_length = 0
    word_count = 0

    f = open(a, 'r')

    for line in f:
        words = line.split()
        for each in words:
            word_length += len(each)
            word_count += 1
    print('Sum of all characters: ', word_length)
    print('Word count: ', word_count)
    print("Average word length: %.2f" % (word_length/word_count))

    f.close()

word_average('D:/python/46excercises/data/palindrome.txt')