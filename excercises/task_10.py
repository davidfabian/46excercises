__author__ = 'd'
'''
Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
'''


def overlapping(a, b):
    result = False
    # check a's first item with all of b's items. Check a's second item, and so on.
    for i in a:
        for k in b:
            if k == i:
                result = True
    print(result)

overlapping([2, "asd", 34, 56, 75, 34, "ASD"], [43, 245, 45, "ASD", 21, 23])