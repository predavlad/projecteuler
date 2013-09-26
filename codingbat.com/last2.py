def last2(str):
    if len(str) < 4:
        return 0
    counter = 0
    for i in range(len(str) - 1):
        if str[i:i + 2] == str[-2:]:
            counter += 1
    return counter - 1

assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2