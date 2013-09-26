def make_bricks(small, big, goal):
    small_len = 1
    big_len = 5
    needed = goal // big_len
    if needed > big:
        needed = big
    goal -= needed * big_len
    if goal <= small:
        return True
    return False


assert make_bricks(3, 2, 10)
assert make_bricks(3, 1, 8)
assert not make_bricks(3, 1, 9)
assert not make_bricks(22, 2, 33)