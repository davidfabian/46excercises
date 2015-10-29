__author__ = 'd'
'''
Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
'''


def wordlength(a):
    result = []
    for i in a:
        result.append(len(i))
    print(result)

wordlength(["fdfd", "ds", "332432", "asdasd"])