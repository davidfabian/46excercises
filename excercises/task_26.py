__author__ = 'd'

'''
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns
the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce()
function directly?
'''


from functools import reduce


def bigger(a, b):
    if a >= b:
        return a
    else:
        return b


def max_in_list(thelist):
    print(reduce(bigger, thelist))
# reduce takes a function and a list. Running the function with the first two items of the list.
# Then the result, and the next item. Until finished
max_in_list([1, 888, 34, 455, 3, 777, 1, 56, 989])