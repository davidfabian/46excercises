__author__ = 'd'

'''
The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of
 the infinitive form: run -> runs. A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s
Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its
third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules
must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the
string method endswith().
'''


def make_3sg_form(a):
    result = ''
    # reg is a flag to set to false if the input is not regular
    reg = True
    # irreg is a list of irregular endings
    irreg = ['o', 'ch', 's', 'sh', 'x', 'y', 'z']
    for i in irreg:
        if a.endswith(i):
            reg = False
            if a.endswith('y'):
                # irregulars ending with y
                result = a[:-1] + 'ies'
            else:
                # all other irregulars
                result = a + 'es'
    if reg:
        result = a + 's'
    print(result)

make_3sg_form("copy")