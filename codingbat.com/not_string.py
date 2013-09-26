def not_string(str):
    if str[0:3] == 'not':
        return str
    return "not " + str

assert not_string('candy') == 'not candy'
assert not_string('x') == 'not x'
assert not_string('not bad') == 'not bad'