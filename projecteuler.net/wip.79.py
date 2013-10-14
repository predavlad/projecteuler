import time
import copy

# 0.002 seconds
# as far as I can tell this doesn't work if there is more than 1 occurrence in
# the passcode
start_time = time.time()


def parse_keylog(keylog):
    """
    We know that every 3 digit key contains 3 characters from the passcode
    The characters are in order, so this means that from the code 317
    3 is before 1, 1 is before 7

    So we make a list that contains all the numbers that need to be before and after the number.
    Will save them in a tuple (before, after)
    """
    keys = {}
    for key in keylog:
        keys.setdefault(key[0], set()).add((None, key[1]))
        keys.setdefault(key[1], set()).add((key[0], key[2]))
        keys.setdefault(key[2], set()).add((key[1], None))

    return keys


def find_first(keys):
    """
    Find the number that has to be the first in the current list
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
    Remove all the instances of n where n is present before the current number
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
    Search for the passcode in the given list of partial passcodes
    """
    first = find_first(keys)
    passcode = ''

    while first is not None:
        passcode += first
        keys = remove_start(first, keys)
        first = find_first(keys)
    return passcode


keylogs = list(set(open('79.txt').read().split("\n")))
parsed_keys = parse_keylog(keylogs)

print find_passcode(parsed_keys)


print time.time() - start_time, "seconds"
