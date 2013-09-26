def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    return False


assert sleep_in(False, False)
assert not sleep_in(True, False)
assert sleep_in(False, True)