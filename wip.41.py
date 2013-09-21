import time
import math

start_time = time.time()


def is_pandigital(nr, n):
    digits = ''.join(map(str, range(1, n + 1)))
    nr = str(nr)
    for i in digits:
        if str(i) not in nr[0:n]:
            return False
        if str(i) not in nr[-n:]:
            return False

    return True


def is_prime(nr):
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True


assert is_pandigital(1423, 4) is True
assert is_pandigital(1423, 5) is False
assert is_pandigital(14235554123, 4) is True
assert is_pandigital(1444, 4) is False
assert is_pandigital(123564987, 9) is True




print time.time() - start_time, "seconds"
