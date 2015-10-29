__author__ = 'd'
'''
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
'''


def histogram(a):
    for item in a:
        for i in range(item):
            print("*", end="")
        print()

histogram([2, 8, 4, 5])