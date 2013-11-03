import numpy
import time
from bisect import bisect

# 0.3 seconds
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


lim = 10 ** 8
primes = get_primes(lim / 2)
semi_primes = 0

for i in xrange(int(len(primes) ** 0.5) + 1):
    diff = lim // primes[i]
    pos = bisect(primes, diff)
    if (pos - i) <= 0:
        continue
    semi_primes += abs(pos - i)

print semi_primes

print time.time() - start_time, "seconds"
