import time
import math

start_time = time.time()


def divisor_number(nr):
    divisors = 0
    limit = int(math.sqrt(nr / 2))

    print "\n", nr, ': ',

    for i in range(1, limit + 1):
        if nr % i == 0:
            divisors += 2

    if limit * limit == nr:
        divisors -= 1

    print divisors,
    return divisors


current = 0
increment = 0

not_found = True
while not_found:
    increment += 1
    current += increment

    if divisor_number(current) > 500:
        not_found = False


print "\n Result is: ", current


print time.time() - start_time, "seconds"
