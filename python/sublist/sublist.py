# determine whether list A is sublist, superlist, equal, or not equal with list B

SUBLIST     = 0
SUPERLIST   = 1
EQUAL       = 2
UNEQUAL     = 3

def check_lists(lista, listb):
    if lista == listb:
        return EQUAL
    stra = ''.join(map(str,lista))
    strb = ''.join(map(str,listb))
    if stra in strb:
        return SUBLIST
    elif strb in stra:
        return SUPERLIST
    else:
        return UNEQUAL
