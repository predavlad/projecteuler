def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


assert monkey_trouble(True, True)
assert monkey_trouble(False, False)
assert not monkey_trouble(True, False)