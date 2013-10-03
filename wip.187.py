import time
import numpy
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


LIMIT = 10 ** 8
primes = get_primes(LIMIT/2)
plen = len(primes)
semi_primes = set()
# squares_limit = int(math.floor(math.sqrt(LIMIT)))
# squares_count = len(get_primes(squares_limit + 1))
squares_count = 1229

# for i in xrange(plen):
#     for j in xrange(i + 1, plen):
#         prod = primes[i] * primes[j]
#         if prod >= LIMIT:
#             break
#         semi_primes.add(prod)

# print semi_primes
print len(semi_primes) + squares_count

print time.time() - start_time, "seconds"
