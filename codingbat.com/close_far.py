def close_far(a, b, c):
    return (abs(a-b) <= 1 and abs(a-c) >= 2 and abs(c-b) >= 2) or (abs(a-c) <= 1 and abs(a-b) >= 2 and abs(b-c) >= 2)

assert close_far(1, 2, 10)
assert not close_far(1, 2, 3)
assert close_far(4, 1, 3)