import time
import math

# 0.045 seconds
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

for i in xrange(286, 100000):
    nr = triangle(i)
    if is_pentagonal(nr) and is_hexagonal(nr):
        print nr
        found = i
        break

print found

##### Another solution that takes 0.08 seconds to run
# lim = 100000
# triangles = set([i * (i + 1) / 2 for i in xrange(286, lim)])
# pentagons = set([i * (3 * i - 1) / 2 for i in xrange(166, lim)])
# hexagons = set([i * (2 * i - 1) for i in xrange(144, lim)])
#
# print set.intersection(hexagons, pentagons, triangles)


print time.time() - start_time, "seconds"
