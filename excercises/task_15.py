__author__ = 'd'
'''
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''


def find_longest_word(a):
    result = 0
    for i in a:
        if len(i) > result:
            result = len(i)
    print(result)

find_longest_word(["", "sd", "s", "", "234sasdsdadasdas"])