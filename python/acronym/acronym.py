#Convert long names into acronyms
#e.g. 'Portable Network Graphics' -> 'PNG'
import re

def abbreviate(input_string):
    temp = re.findall('(?:^|\W)(\w)|(?:[a-z]+)([A-Z])',input_string)
    return ''.join(el for elem in temp for el in elem if el).upper()
