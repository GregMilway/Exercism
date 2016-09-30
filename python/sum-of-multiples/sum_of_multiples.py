#If we list all the natural numbers up to but not including 20 that are
#multiples of either 3 or 5, we get 3, 5, 6 and 9, 10, 12, 15, and 18.
#
#The sum of these multiples is 78.
#
#Write a program that can find the sum of the multiples of a given set of
#numbers.

def sum_of_multiples(limit,mults):
    subtot = []
    for mult in mults:
        if mult:
            subtot.extend([i for i in xrange(1,limit) if i not in subtot and i%mult == 0])
    return sum(subtot)
