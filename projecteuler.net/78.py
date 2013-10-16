import time

# 30 seconds
start_time = time.time()

partitions = {}


def p(n):
    """
    Calculate the number of partitions of number n
    """
    global partitions
    if n == 0:
        return 1
    if n <= 0:
        return 0

    if n in partitions:
        return partitions[n]

    root = int(n ** 0.5) + 1
    parts_sum = 0
    for k in xrange(-root, root):
        if k == 0:
            continue
        pent = n - k * (3 * k - 1) // 2
        if p(pent) < 0:
            continue
        parts_sum += int((-1) ** (k - 1)) * p(pent)

    partitions[n] = parts_sum
    return parts_sum


found, nr, lim = False, 1, 10 ** 6

assert p(5) == 7
assert p(6) == 11
assert p(7) == 15
assert p(8) == 22

while not found:
    nr += 1
    if p(nr) % lim == 0:
        print nr
        break



print time.time() - start_time, "seconds"
