import time
import math

start_time = time.time()

def is_digit_fact(nr):
    nr_str = str(nr)
    sum_digits = 0
    for i in nr_str:
        sum_digits += math.factorial(int(i))

    if sum_digits == nr:
        return True
    return False

rez = []
for i in range(11, 1000001):
    if is_digit_fact(i):
        rez.append(i)

print sum(rez)

print time.time() - start_time, "seconds"
