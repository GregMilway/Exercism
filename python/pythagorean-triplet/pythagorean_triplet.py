#functions that a)determine if 3 distinct numbers are a pythagorean triplet, b) finds triplets within a given range,
#c) finds a 'primitive' pythagorean triplet; 'primitive' implies all three elements are co-prime

from itertools import combinations

def is_triplet(triptup):
    A, B, C = triptup[0]**2, triptup[1]**2, triptup[2]**2
    return A+B == C or A+C == B or B+C == A

def triplets_in_range(sml,lrg):
    return {(a,b,c) for a in range(sml,lrg-1) for b in range(a+1,lrg) for c in range(b+1,lrg+1) if a**2 + b**2 == c**2}

def primitive_triplets(b):
    if b%4:
        raise ValueError('Argument must be multiple of 4')
    mn = int(b/2)
    trips = []
    for m,n in combinations(factors(mn),2):
        if not (is_coprime(m,n) and (m-n)%2):
            continue
        a, c = (m**2 - n**2), (m**2 + n**2)
        trip = tuple(sorted([a,b,c]))
        if is_triplet(trip):
            trips.append(trip)
    return set(trips)

def factors(n):
    facts = sorted(set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup),reverse=True)
    return facts

def is_coprime(x,y):
    #hcf one-liner from http://blog.tosh.me/2011/03/coprime-test.html
    hcf = lambda n1, n2: n1 if n2 == 0 else hcf( n2, n1 % n2 )
    return hcf(x,y) == 1

