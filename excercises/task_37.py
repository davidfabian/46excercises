__author__ = 'd'
'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between
1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

>>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
'''

'''
random number distribution test

dict = {'1': 0, '2':1}
import random
average = 0
freq = {a: 0 for a in range(0,21)}
for i in range(1000):
    x = random.randint(0,20)
    freq[x] += 1
for i in freq:
    print(freq[i])
'''

import random


def guessgame():
    name = input('State your name: ')
    print()
    number = random.randint(1, 20)
    guess_count = 0

    print('Hello, %s' % name)
    print()
    print('Well, there is a number between 1 and 20. You have three guesses.')
    print()

    hit = False
    while not hit:
        guess = int(input('Take a guess!'))
        print()
        guess_count += 1
        if guess > number:
            print(hit, 'The number is smaller than your guess')
        elif guess < number:
            print(hit, 'The number is bigger than your guess')
        elif guess == number:
            hit = True
    print('Yay! Good job %s! %d is the number! '
          'You guessed it in %d guesses.' % (name, number, guess_count))


guessgame()