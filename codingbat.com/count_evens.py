def count_evens(nums):
    return len([i for i in nums if i % 2 == 0])

assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0