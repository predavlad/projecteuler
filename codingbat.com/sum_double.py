def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    return a + b

assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8