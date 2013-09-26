def lucky_sum(a, b, c):
    n = [a, b, c]
    sum = 0
    for i in n:
        if i == 13:
            break
        sum += i
    return sum

assert lucky_sum(1, 2, 3) == 6
assert lucky_sum(1, 2, 13) == 3
assert lucky_sum(1, 13, 3) == 1