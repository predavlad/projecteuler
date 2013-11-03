import time

# 0.001 seconds
start_time = time.time()


def get_max_remainder(a):
    return 2 * a * ((a - 1) / 2)


min_a, max_a = 3, 1001
remainder = [0] * max_a

for a in xrange(min_a, max_a):
    remainder[a] = get_max_remainder(a)


print sum(remainder)

print time.time() - start_time, "seconds"
