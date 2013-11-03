import time

# 0.007
start_time = time.time()

ROW_LEN = 50
MIN_LEN = 3
cache = [0] * 51


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

print(F(ROW_LEN, MIN_LEN))

print time.time() - start_time, "seconds"
