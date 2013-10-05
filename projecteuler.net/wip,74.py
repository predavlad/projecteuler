import time
# 170 seconds, although it can be improved if we count all permutations of a number at the same time, instead of
# going through everything
start_time = time.time()

fact_cache = {}
dig_fact_cache = {}
loop_cache = {}


def fact(n):
    global fact_cache
    if n in [0, 1]:
        return 1
    if n not in fact_cache:
        fact_cache[n] = n * fact(n - 1)
    return fact_cache[n]


def digit_fact_sum(n):
    global dig_fact_cache
    if n in dig_fact_cache:
        return dig_fact_cache[n]
    return sum(map(fact, map(int, str(n))))


def get_loop_count(n):
    global loop_cache

    orig_n = n
    is_loop = False
    chain = {}

    while not is_loop:
        new_n = digit_fact_sum(n)
        chain[n], n = new_n, new_n
        if new_n in chain:
            is_loop = True

    chain_len = len(chain)
    current = orig_n
    while current != new_n:
        loop_cache[current] = chain_len
        current = chain[current]
        chain_len -= 1

    for i in range(chain_len):
        loop_cache[current] = chain_len
        current = chain[current]

    return len(chain)

assert get_loop_count(69) == 5
assert get_loop_count(145) == 1
assert get_loop_count(540) == 2
assert get_loop_count(78) == 4
assert get_loop_count(1479) == 60

LIMIT = 10 ** 3
COUNT = 60
counter = 0


for i in xrange(LIMIT):
    if i not in loop_cache:
        nr = get_loop_count(i)
    if loop_cache[i] == COUNT:
        counter += 1
        if counter % 10 == 0:
            print counter, i

print counter

print time.time() - start_time, "seconds"
