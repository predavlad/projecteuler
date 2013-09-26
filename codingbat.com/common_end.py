def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

assert common_end([1, 2, 3], [7, 3])
assert not common_end([1, 2, 3], [7, 3, 2])
assert common_end([1, 2, 3], [1, 3])