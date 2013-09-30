# damn, couldn't install numpy :(
import math
import time

start_time = time.time()
max_prime = 2000000


def is_prime(nr):
    if nr == 2:
        return True
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True


prime_sum = 0
for i in range(2, max_prime):
    if is_prime(i):
        prime_sum += i


print prime_sum


print time.time() - start_time, "seconds"
