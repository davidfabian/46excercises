__author__ = 'd'

'''
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
Use only higher order functions.
'''


from functools import reduce

def find_longest_word(a):
    result = 0
    for i in a:
        if len(i) > result:
            result = len(i)
    print(result)


find_longest_word(['sdffd', 'sdfrger2', 'rwfdscdda', 'df'])
'''
a = ['sdffd', 'sdfrger2', 'rwfdscdda', 'df']
lengths = map(lambda word: len(word), a)
print(list(lengths))
'''
