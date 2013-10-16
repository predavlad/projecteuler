import time

# 0.8 seconds
start_time = time.time()

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def get_prime_limit(power, lim):
    return int(lim ** (1.0/power)) + 1


limit = 5 * 10 ** 7
primes = {}
numbers = set()

for i in range(2, 5):
    primes[i] = get_primes(get_prime_limit(i, limit))

print get_prime_limit(2, limit)
print get_prime_limit(3, limit)
print get_prime_limit(4 , limit)

for i in primes[2]:
    for j in primes[3]:
        for k in primes[4]:
            n = i ** 2 + j ** 3 + k ** 4
            if n <= limit:
                numbers.add(n)

# print numbers
print len(numbers)

print time.time() - start_time, 'seconds'
