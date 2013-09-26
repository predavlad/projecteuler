def alarm_clock(day, vacation):
    if day in [0, 6] and vacation:
        return 'off'
    if day in [0, 6] or vacation:
        return '10:00'
    return '7:00'

assert alarm_clock(1, False) == '7:00'
assert alarm_clock(5, False) == '7:00'
assert alarm_clock(0, False) == '10:00'