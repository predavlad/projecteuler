import time
import copy

# 0.002 seconds
start_time = time.time()


def parse_keylog(keylog):
    """
    We know that every 3 digit key contains 3 characters from the passcode
    The characters are in order, so this means that from the code 317
    3 is before 1, 1 is before 7
    """
    keys = {}
    for key in keylog:
        keys.setdefault(key[0], set()).add((None, key[1]))
        keys.setdefault(key[1], set()).add((key[0], key[2]))
        keys.setdefault(key[2], set()).add((key[1], None))

    return keys


def find_first(keys):
    """
    Find the number that's most likely to be first
    """
    for i in keys:
        is_first = True
        for s in keys[i]:
            if s[0] is not None:
                is_first = False
        if is_first:
            return i
    return None


def remove_start(n, keys):
    """
    Remove all the instances where n is present before the current number
    """
    del keys[n]
    new_keys = copy.deepcopy(keys)
    for i in keys:
        for s in keys[i]:
            if s[0] == n:
                new_keys[i].discard(s)
    return new_keys


def find_passcode(keys):
    """
    At every iteration I try and find the number that is not preceded by anything,
    and completely remove all occurrences until I stop find a first number.
    """
    first = find_first(keys)
    passcode = ''

    while first is not None:
        passcode += first
        keys = remove_start(first, keys)
        first = find_first(keys)
    return passcode


keylogs = list(set(open('79.txt').read().split("\n")))
keys = parse_keylog(keylogs)

print find_passcode(keys)


print time.time() - start_time, "seconds"
