__author__ = 'd'
'''
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word
or phrase, using all the original letters exactly once; e.g., orchestra = carthorse,
A decimal point = I'm a dot in place. Write a Python program that, when started
1) randomly picks a word w from given list of words,
2) randomly permutes w (thus creating an anagram of w),
3) presents the anagram to the user, and
4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to
work with (say) colour words only. The interaction with the program may look like so:

>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
'''

import re
import random
'''
D:/python/46excercises/data/colors
'''


def anagram(filename):
    print('Anagram guessing game.')
    hit = False
    # gets the list of words from the file specified in the argument with the function list_words
    listofwords = list_words(filename)

    # selects one word from the word list
    goal = listofwords[random.randint(0, (len(listofwords)-1))]

    # shuffles the words letters
    l = list(goal)
    random.shuffle(l)
    goalshuffle = ''.join(l)

    print(goalshuffle)

    # game loop. Runs until the goal word guessed correctly
    while not hit:
        guess = input('What is the original word? ')

        if guess == goal:
            print('yay!')
            hit = True
        else:
            print('nope, guess again. The shuffled word is %s' % goalshuffle)


def list_words(file):
    f = open(file)
    a = []
    for line in f:
        word = re.split('\W+', line)
        for each in word:
            # there must be a better solution to regex only the words. This one lists newlines. This is why length is
            # checked below
            if len(each) > 1:
                a.append(each)
    f.close()
    return a

anagram('D:/python/46excercises/data/colors')
