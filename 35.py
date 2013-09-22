import time
import math
from collections import deque

# run time - 2 seconds
start_time = time.time()


def is_prime(nr):
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True


def is_circular(nr):
    rotation = deque(str(nr))
    if '0' in rotation or '2' in rotation or '4' in rotation or '6' in rotation or '8' in rotation:
        return False

    rotations = [list(rotation)]
    for i in range(1, len(str(nr))):
        rotation.rotate()
        rotations.append(list(rotation))

    for i in range(len(str(nr))):
        to_check = int(''.join(rotations[i]))
        if not is_prime(to_check):
            return False

    return True


def get_circulars_limit(n):
    rez = [2]  # too lazy to do special handling for the only even prime number
    for i in range(3, n + 1):
        if is_circular(i):
            rez.append(i)

    return rez

assert not is_circular(35)
assert is_circular(197)
assert is_circular(17)
assert is_circular(11)
assert len(get_circulars_limit(100)) == 13


rez = get_circulars_limit(1000000)
print rez
print len(rez)

print time.time() - start_time, "seconds"
