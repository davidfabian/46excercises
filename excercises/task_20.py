__author__ = 'd'

'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
that takes a list of English words and returns a list of Swedish words.
'''


def translate(a):
    swdict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    result = []
    for i in a:
        if i in swdict:
            result.append(swdict[i])
    print(result)

translate(["Wish", "you", "a", "happy", "new", "year"])