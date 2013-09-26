def left2(str):
    return str[2:] + str[0] + str[1]

assert left2('Hello') == 'lloHe'
assert left2('java') == 'vaja'
assert left2('Hi') == 'Hi'