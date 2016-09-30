# check a given string is a pangram - a string containing all the letters from a-z
from string import ascii_lowercase

def is_pangram(input_string):
    if len(input_string) < 1:
        return False
    charset = set([char for char in input_string.lower() if char in ascii_lowercase])
    if len(charset) == 26:
        return True
    else:
        return False
