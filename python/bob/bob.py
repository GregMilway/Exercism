#
# Skeleton file for the Python "Bob" exercise.
#
#Bob answers 'Sure.' if you ask him a question.
#
#He answers 'Whoa, chill out!' if you yell at him.
#
#He says 'Fine. Be that way!' if you address him without actually saying
#anything.
#
#He answers 'Whatever.' to anything else.

#Precedence is: Shouting > Question > 'empty' string > anything else
import re

def is_shouting(phrase):
    return phrase.isupper()

def is_question(phrase):
    return phrase != '' and phrase[-1] == '?'

def is_non_sentence(phrase):
    phrase = ''.join(filter(None, re.split("[, \-!?:.\']+",phrase)))
    return not phrase.isalnum()

def hey(what):
    what = what.strip()
    if is_shouting(what):
        return 'Whoa, chill out!'
    elif is_question(what):
        return 'Sure.'
    elif is_non_sentence(what):
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
