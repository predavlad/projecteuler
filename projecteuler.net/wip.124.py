import time
import math

# not done yet
start_time = time.time()

cache = {}

def expo(p):
    if p in [1, 2, 3]:
        return p - 1
    global cache
    if p in cache:
        return cache[p]

    root = int(math.floor(math.sqrt(p)))
    total = expo(root)
    while 2 * root <= p:
        cache[root] = total
        root *= 2
        total += 1

    if root == p:
        cache[p] = total
        return total
    else:
        new_r = p - root
        if new_r in cache:
            total += 1
        else:
            total += expo(new_r)
        cache[p] = total
        return total


def get_expo(p):
    global cache
    cache = {}
    return expo(p)


assert get_expo(15) == 5
assert get_expo(16) == 4
print get_expo(24)

print time.time() - start_time, "seconds"
