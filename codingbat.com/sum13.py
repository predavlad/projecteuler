def sum13(nums):
    if len(nums) == 0:
        return 0
    ignore_next = False
    sum = 0
    for i in nums:
        if not ignore_next:
            if i == 13:
                ignore_next = True
            else:
                sum += i
        else:
            ignore_next = False
    return sum

assert sum13([1, 2, 2, 1]) == 6
assert sum13([1, 1]) == 2
assert sum13([1, 2, 2, 1, 13]) == 6