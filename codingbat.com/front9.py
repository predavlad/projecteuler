def array_front9(nums):
    if len(nums) > 4:
        nums = nums[0:4]
    return 9 in nums

assert array_front9([1, 2, 9, 3, 4])
assert not array_front9([1, 2, 3, 4, 9])
assert not array_front9([1, 2, 3, 4, 5])