def string_match(a, b):
    l = min(len(a), len(b))
    a = a[0:l]
    b = b[0:l]
    counter = 0
    for i in range(l-1):
        if a[i:i+2] == b[i:i+2]:
            counter += 1
    return counter

assert string_match('xxcaazz', 'xxbaaz') == 3
assert string_match('abc', 'abc') == 2
assert string_match('abc', 'axc') == 0