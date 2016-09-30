# create functions to sing Twelve Days of Christmas
# verse(n): output nth verse
# verse(m,n): output verse m to n
# sing(): output entire song

nth_days = {1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth'}
nth_line = {1:'a Partridge in a Pear Tree.\n',
            2:'two Turtle Doves, ',
            3:'three French Hens, ',
            4:'four Calling Birds, ',
            5:'five Gold Rings, ',
            6:'six Geese-a-Laying, ',
            7:'seven Swans-a-Swimming, ',
            8:'eight Maids-a-Milking, ',
            9:'nine Ladies Dancing, ',
            10:'ten Lords-a-Leaping, ',
            11:'eleven Pipers Piping, ',
            12:'twelve Drummers Drumming, '}

def verse(n):
    outstring = 'On the {} day of Christmas my true love gave to me, '.format(nth_days[n])
    for nth in range(n,1,-1):
        outstring += nth_line[nth]
    if n > 1:
        outstring += 'and '
    outstring += nth_line[1]
    return outstring

def verses(m,n):
    outstring = ''
    for nth in range(m,n+1):
        outstring += verse(nth) + '\n'
    return outstring

def sing():
    return verses(1,12)
