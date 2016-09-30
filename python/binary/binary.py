# create a binary parser from first principles

def parse_binary(instring):
    if any(el not in '01' for el in instring):
        raise ValueError("Input must be a string of 1's and 0's only")
    tot = 0
    for n, el in enumerate(map(int,instring)[::-1]):
        tot += el*(2**n)
    return tot
