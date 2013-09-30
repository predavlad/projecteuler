import time
import math
import itertools

start_time = time.time()

def is_prime(nr):
    nr = int(nr)
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True

pand = '1234567'  # largest one is 7 digits long
max_found = 0

for i in itertools.permutations(pand):
    if is_prime(''.join(i)):
        if i > max_found:
            max_found = i

print ''.join(max_found)

print time.time() - start_time, "seconds"
