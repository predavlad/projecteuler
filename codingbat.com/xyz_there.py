def xyz_there(str):
    if len(str) <= 3 and str != 'xyz':
        return False
    if str.find('xyz') == 0:
        return True
    if str.find('xyz') == -1:
        return False
    c = 0
    for i in range(1, len(str) - 2):
        if str[i:i+3] == 'xyz' and str[i - 1] != '.':
            c += 1
    return bool(c)

assert xyz_there('abcxyz')
assert not xyz_there('abc.xyz')
assert xyz_there('xyz.abc')
assert xyz_there('abc.xyzxyz')