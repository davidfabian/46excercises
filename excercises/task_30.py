__author__ = 'd'

'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate
your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate()
that takes a list of English words and returns a list of Swedish words.
'''


# this does not work if there ara any words that are not in the dictionary
sweng = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}


def translate(a):
    result = map(lambda item: sweng[item], a)
    print(list(result))

translate(['merry', 'merry', 'new'])