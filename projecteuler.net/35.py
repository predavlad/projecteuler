import time
from collections import deque

# 1.1 seconds, of which 0.3 is the prime generation
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
        for j in xrange(1, n // i):
            primes[j * i] = 1


def prime_rotation(rot):
    return int(''.join(rot)) in primes


def is_circular(n):
    """
    Check if a number is circular (all rotations of it's letters are prime)
    """
    global primes
    rotation = deque(str(n))
    if '0' in rotation or '2' in rotation or '4' in rotation or '6' in rotation or '8' in rotation:
        return False

    if not prime_rotation(rotation):
        return False
    for i in xrange(1, len(str(n))):
        rotation.rotate()
        if not prime_rotation(rotation):
            return False

    return True


def get_circulars_limit(n):
    """
    Get circular numbers under n
    """
    for i in xrange(3, n + 1, 2):
        if is_circular(i):
            yield i


lim = 10 ** 6
primes = set(get_primes(lim))

print len(list(get_circulars_limit(lim)))

print time.time() - start_time, "seconds"
