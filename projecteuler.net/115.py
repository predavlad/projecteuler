import time

start_time = time.time()

MAX_ROW_LEN = 500
MIN_LEN = 50
cache = [0] * (MAX_ROW_LEN + 1)


def F(bsize, csize):
    global cache
    solutions = 1
    if csize > bsize:
        return solutions

    if cache[bsize] != 0:
        return cache[bsize]

    for position in range(0, bsize - csize + 1):
        for blen in range(csize, bsize - position + 1):
            solutions += F(bsize - position - blen - 1, csize)
    cache[bsize] = solutions
    return solutions


for n in range(50, MAX_ROW_LEN):
    current = F(n, MIN_LEN)
    if current > 1000000:
        print n
        break

print time.time() - start_time, "seconds"
