# functions to 1) interpret a binary string or number into a sequence of "handshake" actions, 2) interpret a sequence of actions into a binary string

#1 = wink
#10 = double blink
#100 = close your eyes
#1000 = jump
#10000 = Reverse the order of the operations in the secret handshake.

#invalid binary strings and negative numbers are to be treated as 0

codestring = ['wink', 'double blink', 'close your eyes', 'jump']

def handshake(num):
    #Pythonic type-checking :)
    try:
        num = int(num,2)
    except ValueError:
        num = 0
    except TypeError:
        pass
    if num < 1:
        return []
    outstring = [codestring[n] for n in range(4) if num & (2**n)]
    if num & 16:
        outstring.reverse()
    return outstring

def code(in_string):
    outcode = 0
    for action in in_string:
        if action not in codestring:
            return '0'
        outcode += 2**(codestring.index(action))
    if len(in_string) > 1 and in_string == handshake(outcode)[::-1]:
        outcode += 16
    return format(outcode,'b')
