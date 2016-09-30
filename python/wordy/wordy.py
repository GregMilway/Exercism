#create an interpreter to process word problems

def calculate(word_prob):
    """Takes a maths word problem, and calculates left-to-right
    ignoring operator precedence"""
    prob_list = validate_input(word_prob)
    if not prob_list:
        raise ValueError('Malformed or invalid word problem')
    tot = None
    op = None
    next = None
    for elem in prob_list:
        if tot is None:
            try:
                tot = int(elem)
            except:
                raise ValueError('Missing first number')
        else:
            try:
                next = int(elem)
            except:
                op = elem
        if op is None or next is None:
            continue
        tot = perform_op(tot,next,op)
        next = None
        op = None
    return tot


def perform_op(x,y,op):
    """performs word operator on inputs.
    Raises ValueError if operator is invalid."""
    if op == 'plus':
        return x+y
    elif op == 'minus':
        return x-y
    elif op == 'multiplied':
        return x*y
    elif op == 'divided':
        return x/y
    else:
        raise ValueError('Invalid Operator')

def validate_input(inp):
    """Checks for valid structure of a word problem and
    returns formatted list if valid, empty list if not."""
    if not inp.startswith('What is '):
        return []
    word_prob = [elem for elem in inp[8:].rstrip('?').split() if elem != 'by']
    for elem in word_prob[::2]:
        try:
            int(elem)
        except:
            return []
    return word_prob
