def cat_dog(str):
    c = d = 0
    for i in range(len(str) - 2):
        if str[i:i+3] == 'cat':
            c += 1
        if str[i:i + 3] == 'dog':
            d += 1
    return c == d

assert cat_dog('catdog')
assert not cat_dog('catcat')
assert cat_dog('1cat1cadodog')