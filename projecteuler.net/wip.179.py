import time
import math

start_time = time.time()


def count_divisors(n):
    lim = int(math.floor(math.sqrt(n))) + 1
    counter = 0

    for i in range(1, lim):
        if n % i == 0:
            counter += 2
    return counter


assert count_divisors(10) == 4

prev = 2
nums = 0
for i in range(3, 10 ** 7):
    current = count_divisors(i)
    if current == prev:
        nums += 1
    prev = current
    if i % 10 ** 4 == 0:
        print i

print nums

print time.time() - start_time, "seconds"
