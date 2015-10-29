__author__ = 'd'

'''
Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return
the string "gnitset ma I".
'''


def reverse(a):
    result = ""
    for i in range((len(a)-1), -1, -1):
        result += (a[i])
    return result

# reverse("I am testing.")