import time

# ~200 seconds
start_time = time.time()


def get_next(n):
    """
    Get the sum of digit squares
    """
    return sum([int(i) ** 2 for i in str(n)])


def set_cache(lst, val):
    global cached
    for i in lst:
        cached[i] = val


def get_rez(n):
    global cached
    new_n = n
    old_n = [n]
    while new_n != 1 and new_n != 89:
        if new_n in cached:
            set_cache(old_n, cached[new_n])
            return new_n
        else:
            new_n = get_next(new_n)
    return new_n


cached = {}

assert get_next(44) == 32
assert get_next(89) == 145
assert get_rez(89) == 89
assert get_rez(1) == 1
assert get_rez(32) == 1


count_89 = 0

for i in xrange(1, 10 ** 7):
    rez = get_rez(i)
    if rez == 89:
        count_89 += 1
    if i % 100000 == 0:
        print i, count_89

print count_89


print time.time() - start_time, "seconds"
