import math


def is_prime(nr):
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True


def get_prime_no(pos):
    current_pos = 1
    current_no = 2
    while pos != current_pos:
        current_no += 1
        if is_prime(current_no):
            current_pos += 1

    return current_no

print get_prime_no(10001)


