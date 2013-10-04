import time
import math

# 2.5 seconds
start_time = time.time()


# generates all primes smaller than n
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# check if 2 numbers are permutations of each other
def is_permutation(a, b):
    a = list(str(a))
    b = str(b)
    while a:
        letter = a.pop()
        b = b.replace(letter, '', 1)

    if len(b) == 0:
        return True
    return False

# get all primes composed of 4 digits
primes = get_primes(10001)
primes = primes[168:]

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        prime_a = primes[i]
        prime_b = primes[j]
        if is_permutation(prime_a, prime_b):
            prime_c = 2 * prime_b - prime_a
            if is_permutation(prime_a, prime_c):
                if is_prime(prime_c):
                    print prime_a, prime_b, prime_c



print time.time() - start_time, "seconds"
