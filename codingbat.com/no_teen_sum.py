def fix_teen(n):
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    return n


def no_teen_sum(a, b, c):
    n = [a, b, c]
    sum = 0
    for i in n:
        sum += fix_teen(i)
    return sum

assert no_teen_sum(1, 2, 3) == 6
assert no_teen_sum(2, 13, 1) == 3
assert no_teen_sum(2, 1, 14) == 3