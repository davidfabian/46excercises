__author__ = 'd'
'''
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
'''


def palindrome(a):
    result = True
    for i in range(0, (len(a))//2):
        # this tests the two items located from the same distance form both ends of the word. If same, result will be
        # multiplied by one, if not, by zero. When done, the result is either 0 or 1. 1 means all letters in respective
        # places are the same
        result *= a[i] == a[(len(a)-1)-i]
    print(result == 1)

palindrome("radar0radar")