# function to check for perfect numbers.
# a perfect number, n is one such that its' factors sum to n
# e.g. 6 -> 1, 2, 3, 1+2+3 == 6

def factors(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def is_perfect(n):
    facts = factors(n)
    facts.discard(n)
    return sum(facts) == n
