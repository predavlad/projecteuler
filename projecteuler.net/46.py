import time
import math

# 0.01 seconds
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


double_squares = [2 * i ** 2 for i in range(1, 1000)]
primes = set(get_primes(10000))

for i in xrange(21, 10000, 2):
    if i in primes:
        continue

    found = False
    for key in xrange(1, int(math.sqrt(i // 2)) + 1):
        if i - 2 * (key**2) in primes:
            found = True
            break

    if not found:
        print i
        break


print time.time() - start_time, "seconds"
