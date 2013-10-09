import time

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


counter = 0
for i in get_primes(200000):
    counter += 1
    if counter == 10001:
        print i
        break

print counter


print time.time() - start_time, "seconds"
