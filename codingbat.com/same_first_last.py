def same_first_last(nums):
    if len(nums) == 0:
        return False
    if len(nums) == 1:
        return True
    return nums[0] == nums[-1]

assert not same_first_last([1, 2, 3])
assert same_first_last([1, 2, 3, 1])
assert same_first_last([1, 2, 1])