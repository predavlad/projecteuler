import math
import time

start_time = time.time()


def prime_factors(nr):
    limit = int(math.sqrt(nr))

    for i in range(2, limit):
        if nr % i == 0:
            yield i
        while nr % i == 0:
            nr /= i

nr = 600851475143
print max([i for i in prime_factors(nr)])


print time.time() - start_time, "seconds"
