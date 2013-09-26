def love6(a, b):
    return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6

assert love6(6, 4)
assert not love6(4, 5)
assert love6(1, 5)