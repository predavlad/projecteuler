def round_10(num):
    if num % 10 >= 5:
        return (num // 10 + 1) * 10
    return (num // 10) * 10


def round_sum(a, b, c):
    n = [a, b, c]
    sum = 0
    for i in n:
        sum += round_10(i)
    return sum

assert round_10(18) == 20
assert round_10(12) == 10
assert round_10(15) == 20

assert round_sum(16, 17, 18) == 60
assert round_sum(12, 13, 14) == 30
assert round_sum(6, 4, 4) == 10