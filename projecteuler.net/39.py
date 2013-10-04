import time
import math

# 0.1 seconds
start_time = time.time()


def is_whole(n):
    return n % 1 == 0


def float_eq(n):
    return abs(int(n) - n) <= 0


def get_b(a, p):
    a, b = float(a), float(p)
    return (p ** 2 - 2 * p * a) / (2 * p - 2 * a)


assert get_b(20, 120) == 48

max_nr = 0
max_solutions = 0

for p in range(20, 1000, 2):
    count = 0
    for a in range(1, int(p / 3) + 1):
        b = get_b(a, p)
        if is_whole(b) and a <= b:
            c = math.sqrt(a ** 2 + b ** 2)
            count += 1
            # print p, a, b, c
    if count > max_solutions:
        max_solutions = count
        max_nr = p

print max_solutions, max_nr

print time.time() - start_time, "seconds"