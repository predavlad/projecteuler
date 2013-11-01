import time
import math

# 2.5 seconds
start_time = time.time()


def divisor_number(nr):
    return sum([2 for i in xrange(1, int(math.sqrt(nr / 2))) if nr % i == 0])


found, current, increment = 0, 0, False
while not found:
    increment += 1
    current += increment

    if divisor_number(current) > 500:
        found = True


print "\nResult is: ", current


print time.time() - start_time, "seconds"
