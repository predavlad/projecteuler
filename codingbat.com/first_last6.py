def first_last6(nums):
    if len(nums) == 1:
        return nums[0] == 6
    return nums[0] == 6 or nums[-1] == 6

assert first_last6([1, 2, 6])
assert first_last6([6, 1, 2, 3])
assert not first_last6([13, 6, 1, 2, 3])