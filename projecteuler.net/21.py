import math
import time

# 2.5 seconds
start_time = time.time()


def get_proper_divisors(nr):
    divisors = [1]
    for i in range(2, int(math.floor(nr / 2)) + 1):
        if nr % i == 0:
            divisors.append(i)

    return divisors


def is_amicable_number(nr):
    divisors = get_proper_divisors(nr)
    amicable_nr = sum(divisors)

    if amicable_nr != nr and sum(get_proper_divisors(amicable_nr)) == nr:
        return True

    return False


amicable_numbers = []

for i in range(1, 10001):
    if is_amicable_number(i):
        amicable_numbers.append(i)

print amicable_numbers
print sum(amicable_numbers)


print time.time() - start_time, "seconds"
