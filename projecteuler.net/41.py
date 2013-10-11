import time
import math
from itertools import permutations

# 0.17 seconds
start_time = time.time()


def is_prime(n):
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


# the largest 1-n pandigital prime is 7 digits long
pand = '1234567'
max_found = 0

for i in permutations(pand):
    n = int(''.join(i))
    if is_prime(n):
        max_found = max(n, max_found)


print max_found

print time.time() - start_time, "seconds"
