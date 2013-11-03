import time

# 0.36 seconds
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


def get_remainder(p, n):
    if n % 2 == 0:
        return 2
    return 2 * n * p


primes = list(get_primes(10 ** 6))

for i in xrange(len(primes)):
    power = i + 1
    if power % 2 == 0:
        continue
    rem = get_remainder(primes[i], power)
    if rem > 10 ** 10:
        print power
        break

print time.time() - start_time, "seconds"
