import time
from fractions import gcd
from itertools import combinations, count
from math import hypot

start_time = time.time()


def primitive_pythagorean_triples(max_side):
    """Generate the primitive Pythagorean triples whose shortest side is
    no longer than max_side.

    """
    for m, n in combinations(xrange(1, max_side // 2 + 3), 2):
        if (m - n) % 2 and gcd(m, n) == 1:
            a = n ** 2 - m ** 2
            b = 2 * m * n
            c = n ** 2 + m ** 2
            if a < b and a <= max_side:
                yield a, b, c
            elif b < a and b <= max_side:
                yield b, a, c


def pythagorean_pairs(max_side):
    """Generate pairs of integers (a, b), where a is the short leg and b
    the long leg of a Pythagorean triangle, and where a <= max_side
    and b <= 2 * max_side.

    """
    for a, b, _ in primitive_pythagorean_triples(max_side):
        for k in count(1):
            ka, kb = k * a, k * b
            if ka > max_side or kb > 2 * max_side:
                break
            yield ka, kb


def count_cuboids(a, b):
    """Given a Pythagorean pair (a, b), return the number of cuboids (p, q, r)
    such that 1 <= p, q, r <= LIMIT and
    either: p <= q <= b and p + q == a
    or: q <= r <= a and q + r == b.

    """
    shorter = a
    longer = b
    counter = 0
    # when M is shorter, let's count ways to split longer
    # i.e. for triple (6,8,10)
    # shorter is 6, longer is 8
    # we set M to 6, and we want to split 8 into (6,2),  (5,3), (4,4)
    output = {}
    base = longer / 2
    if shorter > base:
        counter += shorter - base + 1 - (longer % 2)
    base2 = shorter / 2
    counter += shorter - base2 - (shorter % 2)
    return counter


def count_cuboids_limit(LIMIT):
    output = 0
    for a, b in pythagorean_pairs(LIMIT):
        print a, b
        output += count_cuboids(a, b)
    return output

output = {}
print count_cuboids_limit(100)



print count_cuboids(6, 8)  # 6
print count_cuboids(3, 4)  # 3
print count_cuboids(8, 15)  # 5
print count_cuboids(15, 36)  # 7
print count_cuboids(65, 72)


print time.time() - start_time, "seconds"
