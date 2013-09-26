def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    return False

assert parrot_trouble(True, 6)
assert not parrot_trouble(True, 7)
assert not parrot_trouble(False, 6)