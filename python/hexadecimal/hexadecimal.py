#convert hexadecimal strings to integers

char_map = {'0':0, '1':1, '2':2, '3':3, '4':4,
            '5':5, '6':6, '7':7, '8':8, '9':9,
            'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

def hexa(in_string):
    in_string = in_string.lower()
    val = 0
    if any(elem not in '0123456789abcdef' for elem in in_string):
        raise ValueError('Input must be a hexadecimal string')
    for n, elem in enumerate(in_string[::-1]):
        val += char_map[elem] * (16**n)
    return val
