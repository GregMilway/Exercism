#create a crypto-square

def get_rowcol(n):
    side = int(n**0.5)
    if side**2 == n:
        return side, side
    elif n <= side**2 + side:
        return side, side+1
    else:
        return side+1, side+1

def normalise(plaintext):
    return ''.join(char.lower() for char in plaintext if char.isalnum())

def pad(chunk,size):
    return chunk+' '*(size - len(chunk))

def encode(plaintext):
    if plaintext == '':
        return ''
    normstr = normalise(plaintext)
    row, col = get_rowcol(len(normstr))
    sqrstr = [normstr[n*col:(n+1)*col] for n in range(row)]
    sqrstr[-1] = pad(sqrstr[-1],col)
    return ' '.join(''.join(sqrstr[r][c] for r in range(row)).rstrip() for c in range(col))
