__author__ = 'd'
'''
Define a function that computes the length of a given list or string. (It is true that Python has the
len() function built in, but writing it yourself is nevertheless a good exercise.)
'''


def length(a):
    d = 0
# "i in a" will go through the argument, if it's a string or a list. string: character-by-character, list: item-by-item.
    for i in a:
        d += 1
    print(d)
'''
length("asdsdfs34f")

length("121212")

length([1, 2, 3, 5, 68, 54, "asd"])
'''