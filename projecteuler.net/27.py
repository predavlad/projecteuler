import time

# 0.5 seconds
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


lim = 1000
max_seq = max_a = max_b = 0
primes = set(i for i in get_primes(lim ** 2 + 2 * lim))
primes_1000 = [i for i in primes if i < lim]

# a can only be odd. If a is even, the generated number will be even IF n is odd
# so the number of consecutive primes will stop at n = 1
for a in xrange(1-lim, lim, 2):
    # for n = 0, b must be prime. So only iterate through primes
    for b in primes_1000:
        n, nr = 0, b
        while nr in primes:
            n += 1
            nr = n ** 2 + n * a + b

        if n > max_seq:
            print n, 'consecutive primes with numbers: ', a, b
            max_seq, max_a, max_b = n, a, b


print "The requested product is:", max_a * max_b

print time.time() - start_time, "seconds"
