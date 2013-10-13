import time
import math
from itertools import combinations

# 0.015 seconds
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


perms = {}
for i in range(10001):
    perms[i] = []

for prime in get_primes(10001):
    pkey = int(''.join(sorted(list(str(prime)))))
    if pkey < 1000:
        continue
    perms[pkey].append(prime)


for i in perms:
    differences = {}
    for a, b, c in combinations(perms[i], 3):
        diffs = set([abs(a - b), abs(b - c), abs(c - a)])
        if len(diffs) != 3:
            print a, b, c




#### Below is my first version, that worked, but took 2.5 seconds
# def is_prime(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# check if 2 numbers are permutations of each other
# def is_permutation(a, b):
#     a = list(str(a))
#     b = str(b)
#     while a:
#         letter = a.pop()
#         b = b.replace(letter, '', 1)
#
#     if len(b) == 0:
#         return True
#     return False
#
# # get all primes composed of 4 digits
# primes = list(get_primes(10001))
# primes = primes[168:]
#
# for i in range(len(primes)):
#     for j in range(i + 1, len(primes)):
#         prime_a = primes[i]
#         prime_b = primes[j]
#         if is_permutation(prime_a, prime_b):
#             prime_c = 2 * prime_b - prime_a
#             if is_permutation(prime_a, prime_c):
#                 if is_prime(prime_c):
#                     print prime_a, prime_b, prime_c



print time.time() - start_time, "seconds"
