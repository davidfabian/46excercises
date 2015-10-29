__author__ = 'd'
'''
Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.
'''

from task_7 import reverse


def palindrome_checker(a):
    return converter(a) == reverse(converter(a))


def converter(a):
    temp = ""
    ignorelist = ["'", ",", ".", "?", "!", ";", " ", "’"]
    for i in a.lower():
        for k in ignorelist:
            if k == i:
                break
        else:
            temp += i

    return temp

print(palindrome_checker("As I peed, sir, I see Pisa."))