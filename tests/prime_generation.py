import time
import numpy

start_time = time.time()


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


print get_primes(999999)


print time.time() - start_time, "seconds"
