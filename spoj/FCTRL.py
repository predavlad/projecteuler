import time
start_time = time.time()

# works, but not fast enough
n = int(raw_input(""))
cache = {}


def Z(n):
    pow2 = 0
    pow5 = 0
    for i in xrange(n, 2, -1):
        if i in cache:
            pow2 += cache[i]
            pow5 += cache[i]
            break
        else:
            temp = i
            while temp % 2 == 0:
                pow2 += 1
                temp /= 2
            while temp % 5 == 0:
                pow5 += 1
                temp /= 5
    cache[n] = min(pow2, pow5)
    return min(pow2, pow5)


for i in range(n):
    n = int(raw_input(""))
    print Z(n)

print time.time() - start_time, "seconds"


