import primesieve as ps

primeIter = ps.Iterator()

def prime_factors(n):
    primeIter.skipto(n+1)
    prev_prime = primeIter.previous_prime()
    factors = []
    while n > 1:
        if prev_prime != n and prev_prime > int(n**(0.5)) + 1:
            prev_prime = primeIter.previous_prime()
        if n%prev_prime == 0:
            print prev_prime
            n /= prev_prime
        else:
            prev_prime = primeIter.previous_prime()

