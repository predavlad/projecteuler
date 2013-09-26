def string_splosion(str):
    if len(str) == 0:
        return ''
    ret = ''
    for i in range(1, len(str) + 1):
        ret += str[0:i]
    return ret


assert string_splosion('Code') == 'CCoCodCode'
assert string_splosion('abc') == 'aababc'
assert string_splosion('ab') == 'aab'