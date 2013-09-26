def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if b == c:
        return a
    if a == c:
        return b
    return a + b + c


assert lone_sum(1, 2, 3) == 6
assert lone_sum(3, 2, 3) == 2
assert lone_sum(3, 3, 3) == 0