#Find the difference between the sum of the squares and the square of the sums of the first N natural numbers.
#
#The square of the sum of the first ten natural numbers is,
#
#    (1 + 2 + ... + 10)**2 = 55**2 = 3025
#
#The sum of the squares of the first ten natural numbers is,
#
#    1**2 + 2**2 + ... + 10**2 = 385
#
#Hence the difference between the square of the sum of the first
#ten natural numbers and the sum of the squares is 2640:
#
#    3025 - 385 = 2640

#sum(k**2), k=1 to n, closed form is: 1/6 * n*(n+1)(2*n+1)
#sum(k)^2, k=1 to n, closed form is: (1/2 * n*(n+1))**2

def square_of_sum(n):
    return ((n*(n+1))//2)**2

def sum_of_squares(n):
    return (n*(n+1)*(2*n+1))//6

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
