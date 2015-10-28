__author__ = 'd'
'''
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
should return the string "tothohisos isos fofunon".
'''
vowellist = ["e", "y", "u", "i", "o", "a", " "]

def translate(sentence):
    result=""
    for i in sentence:
        if i in vowellist:
            result=result+(i)
        else:
            result=result+(i+"o"+i)
    print(result)

translate("this is fun")