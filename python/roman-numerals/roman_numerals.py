#convert Arabic numbers to Roman numerals
#e.g. 1996 -> MCMXCVI

ar_mapping = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}

def next_largest(n):
    return max([key for key in sorted(ar_mapping.keys()) if key <= n])

def numeral(n):
    num_string = ''
    while n:
        next_num = next_largest(n)
        num_string += ar_mapping[next_num]
        n -= next_num
    return num_string
