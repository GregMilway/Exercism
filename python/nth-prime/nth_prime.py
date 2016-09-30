#find the nth prime, without using built-ins (including 3rd-party libraries)


def wheel_factor(n):
    small = [2,3,5]
    for prime in small:
        if n%prime == 0:
            return prime
    wheel = [7,11,13,17,19,23,29,31]
    sqrt = int(n**0.5) + 1
    for factor in range(0,sqrt,30):
        for prime in wheel:
            if n%(factor+prime) == 0:
                return (factor + prime)
    return n

def is_prime(n):
    return n == wheel_factor(n)

def nth_prime(n):
    assert n > 0, "There is no zero-th prime!"
    #for small n, check pre-defined list
    small_primes = [2,3,5,7,11,13,17,19,23,29,31]
    if n <= 11:
        return small_primes[n-1]
    count = 11
    candidate = 33
    while True:
        if is_prime(candidate):
            count += 1
        if count == n:
            break
        candidate += 2
    return candidate
