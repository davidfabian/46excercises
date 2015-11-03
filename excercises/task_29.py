__author__ = 'd'

'''
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.
'''


def filter_long_words(a, n):
    result = filter(lambda word: len(word) > n, a)
    print(list(result))

filter_long_words(['dsf', 'sdfdsfsdfs', '23ewrw', 'dd'], 2)