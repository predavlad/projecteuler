import time

# 0.04 seconds
start_time = time.time()


def is_pandigital(nr):
    """
    Check if a number is 1-9 pandigital
    """
    nr = str(nr)
    for i in map(str, range(1, 10)):
        if i not in nr:
            return False
    return True


def is_pandigital_multiple(n, div_list):
    new_nr = ''.join([str(n*div_list[i]) for i in range(len(div_list))])

    if len(new_nr) != 9:
        return False

    if is_pandigital(new_nr):
        return new_nr

    return False


max_pand = 0
for i in xrange(10 ** 3, 10 ** 4):
    for j in xrange(2, 4):
        rez = is_pandigital_multiple(i, range(1, j + 1))
        if rez:
            max_pand = max(max_pand, rez)

print max_pand

print time.time() - start_time, "seconds"
