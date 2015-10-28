__author__ = 'd'
'''
Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else
 construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is
  nevertheless a good exercise.)
'''


def maxi(a,b):
    if a>b:
        print(a)
    if b>a:
        print(b)
    elif(a==b):
        print(a,"=",b)


maxi(24,2)