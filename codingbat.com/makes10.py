def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


assert makes10(9, 10)
assert not makes10(9, 9)
assert makes10(1, 9)