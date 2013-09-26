def string_bits(str):
    counter = 1
    ret = ''
    for i in str:
        if counter % 2:
            ret += i
        counter += 1
    return ret


assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') == 'H'
assert string_bits('Heeololeo') == 'Hello'