def front3(str):
    if len(str) < 3:
        return str * 3
    return str[0:3] * 3


assert front3('Java') == 'JavJavJav'
assert front3('Chocolate') == 'ChoChoCho'
assert front3('abc') == 'abcabcabc'