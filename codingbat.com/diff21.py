def diff21(n):
    if n > 21:
        return 2 * abs(21 - n)
    return abs(21 - n)

assert diff21(19) == 2
assert diff21(10) == 11
assert diff21(21) == 0