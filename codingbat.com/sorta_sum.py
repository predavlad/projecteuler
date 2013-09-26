def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    return a + b

assert sorta_sum(3, 4) == 7
assert sorta_sum(9, 4) == 20
assert sorta_sum(10, 11) == 21