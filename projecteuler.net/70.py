import time

# 30 minutes run time, but it works
start_time = time.time()


def get_divisors(n):
    root = int(n ** 0.5)
    for i in xrange(2, root + 1):
        power = 0
        while n % i == 0:
            power += 1
            n /= i
        if power != 0:
            yield i, power
    # this happens if the number is prime
    if n != 1:
        yield n, 1


def is_permutation(a, b):
    a = list(str(a))
    b = str(b)

    if len(b) != len(a):
        return False

    while a:
        letter = a.pop()
        b = b.replace(letter, '', 1)

    if len(b) == 0:
        return True
    return False


def phi(n):
    ret = n
    for p, power in get_divisors(n):
        ret /= p
        ret *= p - 1
    return ret


min_ratio, number = 10, 0
for i in xrange(2, 10 ** 7):
    j = phi(i)
    ratio = float(i) / j
    if min_ratio > ratio:
        if is_permutation(i, j):
            min_ratio = ratio
            number = i
    if i % 10 ** 5 == 0:
        print i

print min_ratio, number

print time.time() - start_time, "seconds"
