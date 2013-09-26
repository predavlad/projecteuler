def front_back(str):
    if len(str) == 1 or len(str) == 0:
        return str
    return str[-1:] + str[1:len(str)-1] + str[0]

assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'