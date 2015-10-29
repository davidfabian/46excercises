__author__ = 'd'

'''
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
is a pangram or not.
'''


def pangram(a):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

    for i in a.lower():
        if i in abc:
            abc.remove(i)
    print(not len(abc) > 0)

pangram("The Quick Brown Fox Jumps Over The Lazy Dog.")
