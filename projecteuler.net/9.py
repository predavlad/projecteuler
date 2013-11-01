import time
import math
from fractions import gcd
from operator import mul

# 0.0 seconds
start_time = time.time()


def get_pythagorean_primes(lim):
    root = int(math.sqrt(lim)) + 1
    for n in xrange(1, root):
        for m in xrange(n + 1, root):
            if gcd(m, n) == 1 and ((m - n) % 2):
                a, b, c = 2 * m * n, m**2 - n**2, m**2 + n**2
                if c < lim:
                    yield a, b, c


def get_pythagorean_pairs(lim):
    for a, b, c in get_pythagorean_primes(lim):
        k = 1
        while True:
            ka, kb, kc = k * a, k * b, k * c
            k += 1
            if kc > lim:
                break
            yield ka, kb, kc


for i in get_pythagorean_pairs(500):
    if sum(i) == 1000:
        print reduce(mul, i)
        break


print time.time() - start_time, "seconds"
