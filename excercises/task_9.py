__author__ = 'd'

'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns
True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of
the exercise you should pretend Python did not have this operator.)
'''


def is_member(x, a):
    result = False
    for i in a:
        if x == i:
            result = True
    print(result)

is_member(4, [23, "sd", True, 44, 44])