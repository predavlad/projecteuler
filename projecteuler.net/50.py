import time
import math

# 0.5 seconds
start_time = time.time()


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


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


limit = 1000000
primes = list(get_primes(limit))
print 'There are', len(primes), 'primes that we will check.'
max_seq = 0
max_seq_nr = 0


for j in xrange(int(math.sqrt(len(primes)))):
    prime_sum = prime_count = 0
    if max_seq > len(primes[j:]):
        break
    for i in primes[j:]:
        if prime_sum < limit:
            prime_sum += i
            prime_count += 1
            if prime_count > max_seq:
                if is_prime(prime_sum):
                    max_seq, max_seq_nr = prime_count, prime_sum
        else:
            break

print max_seq, max_seq_nr


print time.time() - start_time, "seconds"
