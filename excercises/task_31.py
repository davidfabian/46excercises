__author__ = 'd'
'''
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the
line to the screen if it is a palindrome.
'''

# writes all the palindrome lines from the file


def palindrome(where):
    f = open(where, 'r')

    for line in f:
        res = 0
        if len(line) > 1:
            res = 1
            for i in range(0, len(line)//2):
                res *= (line[i] == line[len(line)-2-i])
        if res == 1:
            print(line, end='')
    f.close()

filename = input('Full path and filename: ')

palindrome(filename)