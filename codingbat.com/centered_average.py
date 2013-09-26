def centered_average(nums):
    nums = list(nums)
    nums.sort()
    nums.pop()
    nums.pop(0)
    return sum(nums) // len(nums)


assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3