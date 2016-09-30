#two functions, to show number of grains on a given chessboard square, and total grains  up to given square

#grains on squares:
#1) 1 = 2**0
#2) 2 = 2**1
#3) 4 = 2**2
#
#Thus, we can see that for any given square, n, the grains on each square is 2**(n-1)
#
#For the total number of grains up to a given square, n, we calculate sum(2**(k-1)), for k = 1 to n.
#This equates to 2**n - 1 (this is equivalent to the maximum value of an n-bit number)

def on_square(n):
    return 2**(n-1)

def total_after(n):
    return 2**n - 1
