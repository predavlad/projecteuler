import math
import time

# 0.3 seconds
start_time = time.time()


def prime_factors(n):
    limit = int(math.sqrt(n))

    for i in range(2, limit):
        if n % i == 0:
            yield i
        while nr % i == 0:
            n /= i

nr = 600851475143
print max([i for i in prime_factors(nr)])


print time.time() - start_time, "seconds"
