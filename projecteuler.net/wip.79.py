import time

start_time = time.time()




def parse_keylog(keylog):
    """
    We know that every 3 digit key contains 3 characters from the passcode
    The characters are in order, so this means that from the code 317
    There is 1 after 3, and 7 after 1
    """
    keys = {}
    for key in keylog:
        if key[0] not in keys:
            keys[key[0]] = [(None, key[1])]
        else:
            keys[0].append((None, key[1]))

        if key[1] not in keys:
            keys[key[1]] = [(key[0], key[2])]
        else:
            keys[key[1]].append((key[0], key[2]))

        if key[2] not in keys:
            keys[key[2]] = [(key[1], None)]
        else:
            keys[key[2]].append((key[1], None))

    return keys

# read keylog file + remove duplicates
# duplicates are not needed since we are looking for the shortest passcode
keylogs = list(set(open('79.txt').read().split("\n")))

keys = parse_keylog(keylogs)
print keys

print time.time() - start_time, "seconds"
