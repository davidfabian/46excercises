__author__ = 'd'

'''
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words
that are longer than n.
'''


def filter_long_words(a, n):
    result = []
    for i in a:
        if len(i) > n:
            result.append(i)
    print(result)

filter_long_words(["wqewq", "234", "vmvmvmvmv", "1234"], 4)