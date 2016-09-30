#count words in a string, and return a dictionary containing the words, and counts

import re

def word_count(input_string):
    temp = re.sub(r'[_\W]',r' ',input_string.decode('utf-8'), flags=re.UNICODE)
    word_dict = {}
    for word in temp.lower().split():
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict
