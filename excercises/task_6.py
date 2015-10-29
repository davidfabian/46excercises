__author__ = 'd'

'''
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a
list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''


def summ(a):
    result = 0
    for i in a:
        result += i
    print(result)


def multiply(a):
    result = 1
    for i in a:
        result *= i
    print(result)

summ([1, 2, 3, 4, 5])
multiply([1, 2, 3, 4, 5, 6])