import time
import math
from collections import deque

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

    rotations = list(rotation)
    for i in range(len(rotation)):
        rotation = rotation.rotate()
        print rotation
        rotations.append(rotation)

    print rotations



rez = []
for i in range(1, 101):
    if is_circular(i):
        rez.append(i)


print time.time() - start_time, "seconds"
