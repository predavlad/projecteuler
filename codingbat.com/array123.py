def array123(nums):
    return 1 in nums and 2 in nums and 3 in nums

assert array123([1, 1, 2, 3, 1])
assert not array123([1, 1, 2, 4, 1])
assert array123([1, 1, 2, 1, 2, 3])