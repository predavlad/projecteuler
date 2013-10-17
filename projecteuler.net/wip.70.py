import time
from operator import mul
from fractions import Fraction

# not done yet
start_time = time.time()

def get_primes(n):
    """
    Get all the primes smaller than n
    """
    primes = [0] * n
    for i in xrange(2, n):
        if primes[i] == 0:
            yield i
        else:
            continue
        for j in xrange(2 * i, n, i):
            primes[j] = 1



#for i in get_primes(10 ** 7):
#    pass


#### below is the brute force version that would probably take 20+ minutes

def get_divisors(n):
    root = int(n ** 0.5)
    for i in xrange(2, root + 1):
        power = 0
        while n % i == 0:
            power += 1
            n /= i
        if power != 0:
            yield i, power
            # this happens if the number is prime
    if n != 1:
        yield n, 1


def is_permutation(a, b):
    a = list(str(a))
    b = str(b)

    if len(b) != len(a):
        return False

    while a:
        letter = a.pop()
        b = b.replace(letter, '', 1)

    if len(b) == 0:
        return True
    return False


def phi(n):
    ret = n
    for p, power in get_divisors(n):
        ret /= p
        ret *= p - 1
        #ret *= (1 - Fraction(1, p))
    return ret

for i in xrange(12, 1000, 12):
    print i, phi(i)

#print phi(12)
#print phi(24)
#print phi(36)
#print phi(7)



#min_ratio, number = 10, 0
#for i in xrange(2, 10 ** 4):
#    j = phi(i)
#    ratio = float(i) / j
#    if min_ratio > ratio:
#        if is_permutation(i, j):
#            min_ratio = ratio
#            number = i
#
#print min_ratio, number

print time.time() - start_time, "seconds"
