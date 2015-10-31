__author__ = 'd'
'''
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
 Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''


def char_freq(a):
    result = {}
    for i in a:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print(result)

char_freq("aaas£\"$£\\\"$4343sdds")