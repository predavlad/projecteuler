import time
# 0.001 seconds run time
start_time = time.time()

fact_cache = {}


def fact(n):
    global fact_cache
    if n in [0, 1]:
        return 1
    if n not in fact_cache:
        fact_cache[n] = n * fact(n - 1)
    return fact_cache[n]


def C(n, r):
    return fact(n) / fact(r) / fact(n-r)


LIMIT = 10 ** 6

counter = 0
for n in range(20, 101):
    for r in range(1, n):
        combs = C(n, r)
        if combs > LIMIT:
            nr = abs(r - (n - r)) + 1
            counter += nr
            print 'C(%d, %d) == C(%d, %d) = %d - counter %d' % (n, r, n, n - r, combs, nr)
            break

print counter


print time.time() - start_time, "seconds"
