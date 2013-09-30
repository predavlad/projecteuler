import time
import math

# ~12 seconds
start_time = time.time()


def is_prime(nr):
    if nr == 2:
        return True
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True


def is_truncatable_prime(nr):
    if not is_prime(nr) or nr < 10 or str(nr)[0] == '1' or str(nr)[-1] == '1':
        return False

    temp = str(nr)
    while len(temp) > 1:
        temp = temp[0:-1]
        if not is_prime(int(temp)):
            return False

    temp = str(nr)
    while len(temp) > 1:
        temp = temp[1:]
        if not is_prime(int(temp)):
            return False

    return True


assert not is_truncatable_prime(11)
assert is_truncatable_prime(3797)
assert is_truncatable_prime(797)
assert not is_truncatable_prime(2)

rez = []
for i in range(1, 1000000):
    if is_truncatable_prime(i):
        rez.append(i)


print rez
print len(rez)
print sum(rez)


print time.time() - start_time, "seconds"
