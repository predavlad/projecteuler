import time
import math

# not done yet, bad approach
start_time = time.time()


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def check_pair_set(prime_pair):
    global primes
    for i in prime_pair:
        for j in prime_pair:
            if i != j:
                a, b = int(str(i) + str(j)), int(str(j) + str(i))
                if not is_prime(a) or not is_prime(b):
                    return False
    return True

def check_two_pair(i, j):
    a, b = int(str(i) + str(j)), int(str(j) + str(i))
    if not is_prime(a) or not is_prime(b):
        return False
    return True


limit = 30000
primes = get_primes(limit)
primes.pop(0)  # remove the prime 2
prime_len = len(primes)
prime_pairs = {}

for i in range(0, prime_len):
    for j in range(i + 1, prime_len):
        p1, p2 = primes[i], primes[j]
        if check_two_pair(p1, p2):

            if p1 not in prime_pairs:
                prime_pairs[p1] = set()
            prime_pairs[p1].add(p2)

            if p2 not in prime_pairs:
                prime_pairs[p2] = set()
            prime_pairs[p2].add(p1)


print prime_pairs



print time.time() - start_time, "seconds"
