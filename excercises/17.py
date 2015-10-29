__author__ = 'd'
'''
Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.
'''

# import 7


def palindrome_checker(a):
    print(converter(a))

#just removes special characters
# needs reverse checking
def converter(a):
    temp = ""
    ignorelist = ["'", ",", ".", "?", "!", ";", " "]
    for i in a.lower():
        for k in ignorelist:
            if k == i:
                break
        else:
            temp += i

    return temp

palindrome_checker("Satan, oscillate my metallic sonatas")
