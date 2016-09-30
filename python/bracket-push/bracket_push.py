#checks whether an expression has balanced brackets

import re
bracket_map = { ')':'(', '}':'{', ']':'['}

def check_brackets(in_string):
    stack = []
    #filter out non-bracket chars for ease of checking
    in_string = re.sub('[^\(\)\{\}\[\]]','',in_string)
    for elem in in_string:
        if elem in '({[':
            stack.append(elem)
        else:
            try:
                last = stack.pop()
            except IndexError: #we have one too many close brackets
                return False
            if last != bracket_map[elem]: #brackets aren't nested correctly
                return False
    else:
        return len(stack) == 0 #do we have any left over open brackets?
