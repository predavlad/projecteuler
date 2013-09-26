def first_two(str):
    if len(str) <= 2:
        return str
    return str[0:2]

assert first_two('Hello') == 'He'
assert first_two('abcdefg') == 'ab'
assert first_two('ab') == 'ab'