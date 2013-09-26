def sum67(nums):
    sum = 0
    ignore_next = False
    for i in nums:
        if not ignore_next:
            if i == 6:
                ignore_next = True
            else:
                sum += i
        elif i == 7:
            ignore_next = False
    return sum

assert sum67([1, 2, 2]) == 5
assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
assert sum67([1, 1, 6, 7, 2]) == 4