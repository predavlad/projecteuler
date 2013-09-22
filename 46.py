import time
import math

start_time = time.time()


# the opposite of is composite
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# generates all primes smaller than n
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(5)
assert not is_prime(10)

double_squares = [2 * i ** 2 for i in range(1, 1000)]
primes = get_primes(10000)

for i in range(20, 10000):
    if i % 2 == 0:
        continue
    if not is_prime(i):
        found = False
        for key, val in enumerate(double_squares):
            if i > val:
                if i - val in primes:
                    found = True
                    break
        if not found:
            print i


print time.time() - start_time, "seconds"
