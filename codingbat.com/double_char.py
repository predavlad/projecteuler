def double_char(str):
    ret = ''
    for i in str:
        ret += i * 2
    return ret

assert double_char('The') == 'TThhee'
assert double_char('AAbb') == 'AAAAbbbb'
assert double_char('Hi-There') == 'HHii--TThheerree'