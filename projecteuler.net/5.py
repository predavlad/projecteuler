import time
import math

# 0.0 seconds
start_time = time.time()


def get_divisors(nr):
    for i in xrange(2, int(math.sqrt(nr)) + 1):
        power = 0
        while nr % i == 0:
            power += 1
            nr /= i
        if power != 0:
            yield i, power
    # this happens if the number is prime
    if nr != 1:
        yield nr, 1


def smallest_multiple(nr):
    all_divisors = {}
    for i in xrange(2, nr):
        for prime, power in get_divisors(i):
            if prime in all_divisors:
                if power > all_divisors[prime]:
                    all_divisors[prime] = power
            else:
                all_divisors[prime] = power
    return all_divisors


all_divisors = smallest_multiple(20)

product = 1
for key in all_divisors:
    product *= key ** all_divisors[key]

print product

print time.time() - start_time, "seconds"
