import time
import math

# 0.38 seconds
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


def is_truncatable_prime(n):
    """
    Receive a prime number as input, and determine if the number is a truncatable primes.
    A truncatable prime means that removing digits from left or right results only in primes
    Ex: 3797 is a truncatable primes:
        - remove digits from right => 3797, 379, 37 and 3 are primes
        - remove digits from left => 3797, 797, 97 and 7 are primes
    """
    global primes
    digit_primes = ['2', '3', '5', '7']
    if n < 10 or str(n)[0] not in digit_primes or str(n)[-1] not in digit_primes:
        return False

    for i in range(1, len(str(n))):
        right, left = int(str(n)[0:i]), int(str(n)[i:])
        if right not in primes or left not in primes:
            return False

    return True


primes = set(get_primes(10 ** 6))  # 1 million is enough
print sum([i for i in primes if is_truncatable_prime(i)])


print time.time() - start_time, "seconds"
