__author__ = 'd'
'''
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its
present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect
such simple rules to work for all cases.
'''
'''
for i in a:
        if i in consonant:
            c += 1
        if i in vowel:
            v += 1
'''


def make_ing_form(a):
    consonant = "qwrtpsdfghjklzxcvbnm"
    # vowel = "euioay"
    if len(a) == 3:
        if a[0] in consonant and a[2] in consonant:
            a += a[2]

    if a.endswith('ie'):
        a = a[:-2]
        a += 'y'
    if a.endswith('e') and not a.endswith('ee'):
        a = a[:-1]

    a += 'ing'
    print(a)

make_ing_form("see")