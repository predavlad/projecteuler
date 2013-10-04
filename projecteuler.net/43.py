import time
from itertools import permutations

# 11 seconds, not the greatest time, but got the job done!
start_time = time.time()


primes = [2, 3, 5, 7, 11, 13, 17]
digits = list(range(0, 10))
pandigitals = list(permutations(digits, len(digits)))
numbers = []


for pand in pandigitals:
    good = True
    for i in range(1, len(pand) - 2):
        current = int(''.join(map(str, pand[i:i+3])))
        if current % primes[i - 1] != 0:
            good = False
            break
    if good:
        good_number = int(''.join(map(str, pand)))
        numbers.append(good_number)


print sum(numbers)

print time.time() - start_time, "seconds"
