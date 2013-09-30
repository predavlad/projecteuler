import time
import math

start_time = time.time()


def is_pentagonal(n):
    return (1 + math.sqrt(1 + (24 * n))) % 6 == 0


def is_hexagonal(n):
    return (1 + math.sqrt(1 + (8 * n))) % 4 == 0


def is_triangle(n):
    return (-1 + math.sqrt(1 + (8 * n))) % 2 == 0


def triangle(n):
    return n * (n + 1) / 2

found = 0

for i in range(286, 100000):
    nr = triangle(i)
    if is_pentagonal(nr) and is_hexagonal(nr):
        print nr
        found = i
        break

print found

print time.time() - start_time, "seconds"
