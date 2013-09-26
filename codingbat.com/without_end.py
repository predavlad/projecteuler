def without_end(str):
    if len(str) == 2:
        return ''
    return str[1:-1]

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'