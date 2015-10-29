__author__ = 'd'
'''
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
'''


def vowel(x):
    vowellist = ["e", "y", "u", "i", "o", "a"]
    if x in vowellist:
        print(True)
    else:
        print(False)

vowel("s")