def make_chocolate(small, big, goal):
    needed = goal // 5
    if needed > big:
        needed = big
    goal -= needed * 5
    if goal > small:
        return -1
    return goal

assert make_chocolate(4, 1, 9) == 4
assert make_chocolate(4, 1, 10) == -1
assert make_chocolate(4, 1, 7) == 2