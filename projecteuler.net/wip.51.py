import time
import math


start_time = time.time()

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in xrange(10 ** 8 + 1, 10 ** 8 + 10 ** 5, 2):
    is_prime(i)


print time.time() - start_time, "seconds"
