# translate english into pig-latin
# if word begins with [a,e,i,o,u], append 'ay' to word e.g. apple -> appleay
# if not, move all consonants before first vowel to end of word and add 'ay'
# special cases:
# 'u' is treated as consonant if  preceded by 'q', eg 'queen' -> 'eenquay', 'square' -> 'aresquay'
# 'y' and 'x' are wild: they can be treated as vowels or consonants, depending on following letter.

import re

def translate(word_string):
    words = word_string.split()
    ordsway = []
    for word in words:
        if re.match('^[aeiou]',word) or word[:2] in 'xryt':
            ordsway.append(word+'ay')
        else:
            if 'qu' in word:
                chunks = filter(None, re.split('(.*qu)',word))
            else:
                chunks = re.split('([aeiou])',word)
            ordsway.append(''.join(chunks[1:])+chunks[0]+'ay')
    return ' '.join(ordsway)
