import time
from fractions import gcd

start_time = time.time()


def get_primes(n):
    """
    Get all the primes smaller than n
    """
    p = [0] * n
    for i in xrange(2, n):
        if p[i] == 0:
            yield i
        else:
            continue
        for j in xrange(1, n // i):
            p[j * i] = 1


def get_divisors(n):
    """
    Get the prime divisors of n
    """
    global primes
    root = int(n ** 0.5) + 1
    i = 0
    is_prime = True
    for prime in primes:
        if n % primes[i] == 0:
            yield primes[i]
            if n / primes[i] in primes:
                yield n / primes[i]
            is_prime = False
        i += 1
    if is_prime:
        yield n


def generate_pairs(n):
    for a in xrange(2, n):
        for b in xrange(i, n):
            if gcd(a, b) == 1:
                c = a + b
                if gcd(a, c) == 1 and gcd(b, c) == 1:
                    yield a, b, c


def rad(n):
    prod = 1
    for div in get_divisors(n):
        prod *= div

lim = 1000
primes = set(get_primes(lim))
set_primes = set(primes)

print list(get_divisors(45616))


print time.time() - start_time, "seconds"
