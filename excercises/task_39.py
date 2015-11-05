__author__ = 'd'
'''
In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by
guessing, and in return receive two kinds of clues:
1) the characters that are fully correct, with respect to identity as well as to position, and
2) the characters that are indeed present in the word, but which are placed in
the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct in
the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2).
Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the
following way:

>>> import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
'''


def lingo(word):
    print('You have to guess a five letter word.')
    print('() shows a right character in the wrong position, [] shows a right character in the right position')
    print('the program finds the same character multiple times.')
    hit = False
    # main game loop
    while not hit:
        guess = input('your guess: ')
        if len(guess) != 5:
            print('the guess have to be FIVE characters long')
        else:
            if guess == word:
                hit = True
                print('YEAH')
            else:
                clue = ['', '', '', '', '']

                # go through letter-by-letter
                for i in range(0, 5):

                    # if matches in position, put in brackets
                    if guess[i] == word[i]:
                        clue[i] = '[' + guess[i] + ']'

                    # if it's in the solution, but in wrong position, put in parenthesis
                    elif guess[i] in word:
                        clue[i] = '(' + guess[i] + ')'

                    # no match, just write it as it was
                    else:
                        clue[i] = ' ' + guess[i] + ' '

                # prints the letters in a more readable format
                for each in clue:
                    print(each, end='')
                print()


lingo('pleen')