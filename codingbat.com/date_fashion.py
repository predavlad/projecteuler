def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

assert date_fashion(5, 10) == 2
assert date_fashion(5, 2) == 0
assert date_fashion(5, 5) == 1