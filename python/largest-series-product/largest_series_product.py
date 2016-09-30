# find the largest product within a series, for a give length
#For example, for the input `'1027839564'`, the largest product for a
#series of 3 digits is 270 (9 * 5 * 6), and the largest product for a
#series of 5 digits is 7560 (7 * 8 * 3 * 9 * 5).

def get_prod(series):
    prod = 1
    for elem in series:
        prod *= int(elem)
    return prod

def largest_product(series, size):
    if series == '' and size > 0:
        raise ValueError('Series must be non-empty string')
    if not series.isdigit() and not series == '':
        raise ValueError('Series must be digit string')
    if size > len(series):
        raise ValueError('Product size must not exceed Series size')
    if size < 0:
        raise ValueError('Product size must be non-negative')
    tot = 0
    end = len(series) - size + 1
    for i in range(end):
        subtot = get_prod(series[i:i+size])
        if subtot > tot:
            tot = subtot
    return tot
