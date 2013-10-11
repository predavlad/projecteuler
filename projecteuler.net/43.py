import time
from itertools import permutations

# 10 seconds, not the greatest time, but got the job done!
# it can be solved without brute force though
start_time = time.time()


primes = [2, 3, 5, 7, 11, 13, 17]
digits = list(range(0, 10))
numbers = 0


for pand in permutations(digits, len(digits)):
    good = True
    for i in xrange(1, len(pand) - 2):
        current = int(''.join(map(str, pand[i:i+3])))
        if current % primes[i - 1] != 0:
            good = False
            break
    if good:
        good_number = int(''.join(map(str, pand)))
        numbers += good_number


print numbers

print time.time() - start_time, "seconds"
