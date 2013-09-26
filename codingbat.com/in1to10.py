def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or 10 <= n
    return n in range(1, 11)

assert in1to10(5, False)
assert not in1to10(11, False)
assert in1to10(11, True)