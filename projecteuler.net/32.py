import time

# 0.1 seconds
start_time = time.time()


def is_pandigital(nr):
    nr = str(nr)
    if len(nr) != 9:
        return False
    digits = set()
    for digit in nr:
        digits.add(digit)
    if len(digits) == 9:
        return True
    return False


def has_intersect(a, b):
    return not set(str(a)).isdisjoint(str(b))


LIMIT = 10 ** 4
products = set()

for i in range(1, LIMIT / 2):
    if i > LIMIT // i or '0' in str(i):
        continue
    for j in range(i + 1, LIMIT / i):
        if has_intersect(i, j) or '0' in str(j):
            continue
        prod = i * j
        if has_intersect(str(i) + str(j), prod) or '0' in str(prod):
            continue
        number = str(i) + str(j) + str(prod)
        if is_pandigital(number):
            print '%d * %d = %d' % (i, j, prod)
            products.add(prod)

print products
print sum(products)



print time.time() - start_time, "seconds"

