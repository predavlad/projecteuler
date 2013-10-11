import time
import math
from fractions import gcd

# 0.001 seconds
start_time = time.time()


def get_pythagorean_primes(lim):
    root = int(math.sqrt(lim)) + 1
    for n in xrange(1, root):
        for m in xrange(n + 1, root):
            if gcd(m, n) == 1 and ((m - n) % 2):
                a, b, c = 2 * m * n, m ** 2 - n ** 2, m ** 2 + n ** 2
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


lim, perim = 1001, {}
max_perim, max_count = 0, 0

for i in range(lim):
    perim[i] = 0


for pyt in get_pythagorean_pairs(lim // 2):
    if sum(pyt) < lim:
        perim[sum(pyt)] += 1


for i in perim:
    if perim[i] > max_count:
        max_count, max_perim = perim[i], i

print max_perim


print time.time() - start_time, "seconds"