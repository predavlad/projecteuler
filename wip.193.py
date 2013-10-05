import numpy
import time
import math
start_time = time.time()

def get_primes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


LIMIT = 2 ** 50
primes = get_primes(int(math.sqrt(LIMIT))+1)
squarefree = LIMIT
not_sq = set()

for i in xrange(len(primes)):
    ps = primes[i] * primes[i]
    diff = LIMIT // ps
    squarefree -= diff


print LIMIT
print squarefree

print 'Seconds', time.time() - start_time
