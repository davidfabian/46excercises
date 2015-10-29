__author__ = 'd'
'''
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for
two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell
in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
'''


def max_in_list(a):
    result = a[0]
    for i in a:
        if i > result:
            result = i
    print(result)

max_in_list([111, 4, 78, 2, 1, 132])