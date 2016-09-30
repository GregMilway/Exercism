#encode and decode with rail-fence cipher
#see read-me for details on implementation
from itertools import izip_longest

def encode(plaintext,n):
    assert n > 0, "Must have at least 1 rail"
    if n == 1:
        return plaintext
    mapping = rail_map(len(plaintext),n)
    return ''.join([plaintext[el] for el in mapping])

def decode(ciphertext,n):
    assert n > 0, "Must have at least 1 rail"
    if n == 1:
        return ciphertext
    ordering = range(len(ciphertext))
    mapping = rail_map(len(ciphertext),n)
    return ''.join([ciphertext[mapping.index(n)] for n in ordering])

def rail_map(length,n):
    step = 2*n -2
    ordering = range(length)
    first = ordering[::step]
    last = ordering[n-1::step]
    middle = []
    for k in range(1,n-1):
        front = ordering[k::step]
        back = ordering[step-k::step]
        line = izip_longest(front,back,fillvalue = None)
        middle.extend([el for elem in line for el in elem if el is not None])
    return first + middle + last
