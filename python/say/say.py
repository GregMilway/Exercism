#convert a number to a string representing the english sentence for that number
#e.g. 1 -> 'one', 22 -> 'twenty-two', 123 -> 'one hundred and twenty-three'

num_words =    {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
                11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
                18:'eighteen',19:'nineteen',
                20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
                100:'hundred',1e3:'thousand',1e6:'million',1e9:'billion',
                0:'zero'}

def div_lt_20(n):
    return num_words[n]

def div_lt_tun(n):
    output = ''
    if n <= 20:
        output += div_lt_20(n)
    else:
        tens, unit = divmod(n, 10)
        output += num_words[tens*10]
        if unit:
            output += '-' + div_lt_20(unit)
    return output

def div_lt_thou(n):
    output = ''
    if n < 100:
        output += div_lt_tun(n)
    else:
        tuns, rem = divmod(n, 100)
        output += num_words[tuns] + ' ' + num_words[100]
        if rem:
            output += ' and ' + div_lt_tun(rem)
    return output

def div_lt_mill(n):
    output = ''
    if n < 1000:
        output += div_lt_thou(n)
    else:
        thou, rem = divmod(n, 1000)
        output += div_lt_thou(thou) + ' ' + num_words[1000]
        if rem:
            if rem < 100:
                output += ' and'
            output += ' ' + div_lt_thou(rem)
    return output

def div_lt_bill(n):
    output = ''
    if n < 1e6:
        output += div_lt_mill(n)
    else:
        mill, rem = divmod(n, 1e6)
        output += div_lt_thou(mill) + ' ' + num_words[1e6]
        if rem:
            if rem < 100:
                output += ' and'
            output += ' ' + div_lt_mill(rem)
    return output

def div_lt_tril(n):
    output = ''
    if n < 1e9:
        output += div_lt_bill(n)
    else:
        bill, rem = divmod(n, 1e9)
        output += div_lt_thou(bill) + ' ' + num_words[1e9]
        if rem:
            if rem < 100:
                output += ' and'
            output += ' ' + div_lt_bill(rem)
    return output

def say(n):
    if not 0 <= n < 1e12:
        raise AttributeError()
    else:
        return div_lt_tril(n)
