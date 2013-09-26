def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a == b:
        return True
    l_a = len(a)
    l_b = len(b)
    if l_a > l_b:
        if b == a[l_a - l_b:]:
            return True
    if a == b[l_b - l_a:]:
        return True
    return False

assert end_other('Hiabc', 'abc')
assert end_other('AbC', 'HiaBc')
assert end_other('abc', 'abXabc')
assert not end_other('abc', 'abXxbc')