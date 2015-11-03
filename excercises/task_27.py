__author__ = 'd'

'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and
3) using list comprehensions.
'''


# simple for loop
def lenlist1(lista):
    result = []
    for i in lista:
        result.append(len(i))
    print(result)


# lambda and map()
def lenlist2(lista):
    i = lambda x: (len(lista[x]))
    result = list(map(i, range(len(lista))))
    print(result)


# list comprehension
a = ['ewrw', 'cwewd3d', '23dsc', 'ddew']
lenlist3 = [len(a[x]) for x in range(len(a))]
print(lenlist3)

# testing
lenlist1(['ewrw', 'cwewd3d', '23dsc', 'ddew'])
lenlist2(['ewrw', 'cwewd3d', '23dsc', 'ddew'])