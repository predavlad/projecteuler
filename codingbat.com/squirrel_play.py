def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    return 60 <= temp <= 90

assert squirrel_play(70, False)
assert not squirrel_play(95, False)
assert squirrel_play(95, True)