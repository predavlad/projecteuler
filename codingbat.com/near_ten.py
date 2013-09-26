def near_ten(num):
    return num % 10 in [0, 1, 2, 8, 9]

assert near_ten(12)
assert not near_ten(17)
assert near_ten(19)