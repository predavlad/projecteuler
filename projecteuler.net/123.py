import time

start_time = time.time()


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def get_remainder(p, n):
    if n % 2 == 0:
        return 2
    return 2 * n * p


primes = get_primes(1000000)

for i in range(len(primes)):
    power = i + 1
    if power % 2 == 0:
        continue
    rem = get_remainder(primes[i], power)
    if rem > 10 ** 10:
        print power
        break

print time.time() - start_time, "seconds"
