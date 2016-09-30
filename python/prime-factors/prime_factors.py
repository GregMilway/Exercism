#generate list of prime factors for a given composite number, as follows:
# [a a b c d d e f g] = prime_factors(X)

import primesieve as ps

primeIter = ps.Iterator()

def prime_factors(n):
    primeIter.skipto(0)
    next_prime = primeIter.next_prime()
    factors = []
    while n > 1:
        if n%next_prime == 0:
            factors.append(next_prime)
            n /= next_prime
        else:
            next_prime = primeIter.next_prime()
    return factors

