import math
import time

# 2.5 seconds
start_time = time.time()


def divisor_sum(n):
    return sum(get_proper_divisors(n))


def get_proper_divisors(n):
    yield 1
    for i in xrange(2, int(math.floor(n / 2)) + 1):
        if n % i == 0:
            yield i


def is_amicable_number(n):
    amicable_nr = divisor_sum(n)
    return amicable_nr != n and divisor_sum(amicable_nr) == n


print sum([i for i in range(1, 10001) if is_amicable_number(i)])



print time.time() - start_time, "seconds"
