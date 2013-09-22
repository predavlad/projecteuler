import time
import math

start_time = time.time()

def digit_sum(n):
    n = str(n);
    dig_sum = 0
    for i in n:
        dig_sum += int(i)
    return dig_sum

assert digit_sum(22) == 4
assert digit_sum(999) == 27

max_digit_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        current_sum = digit_sum(a ** b)
        max_digit_sum = max(max_digit_sum, current_sum)

print max_digit_sum

print time.time() - start_time, "seconds"
