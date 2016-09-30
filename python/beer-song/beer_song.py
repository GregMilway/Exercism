#functions to sing the beer-bottle song (99 bottles of beer on the wall...)

def verse(num):
    def numstr(n):
        if n == -1:
            return '99'
        elif n == 0:
            return 'no more'
        else:
            return str(n)

    def bottlestr(n):
        return 'bottle' if n == 1 else 'bottles'

    def takestr(n):
        return 'it' if n == 1 else 'one'

    first = '{0} {1} of beer on the wall, {0} {1} of beer.\n'.format(numstr(num),bottlestr(num)).capitalize()
    second = 'Go to the store and buy some more,' if num == 0 else 'Take {} down and pass it around,'.format(takestr(num))
    third = ' {0} {1} of beer on the wall.\n'.format(numstr(num-1),bottlestr(num-1))

    return first+second+third



def song(start,end=0):
    return '\n'.join(verse(n) for n in range(start,end-1,-1)) + '\n'
