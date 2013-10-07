import time
import math

### Not working yet.
start_time = time.time()


def get_divisors(nr):
    divisors = {}
    for i in range(2, nr + 1):
        nrDiv = 0
        while nr % i == 0:
            nrDiv += 1
            nr /= i
        if nrDiv != 0:
            divisors[i] = nrDiv
    return divisors


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# this avoids multiple divisor search for the same number
def get_cached_divisors(n):
    global cached_divisors
    if n in cached_divisors:
        divisors = cached_divisors[n]
    else:
        divisors = get_divisors(n)
        cached_divisors[n] = divisors

    rez = {}
    for key, val in enumerate(divisors):
        v = str(key) + '-' + str(val)
        rez[v] = v

    return rez


# get first consecutive n numbers to have n distinct prime factors
def get_consecutive(n):
    numbers = range(n)
    for i in range(n, 1500000):
        if i % 10000 == 0:
            print 'Reached %d numbers.' % i
        del numbers[0]
        numbers.append(i)
        all_divisors = []
        for key, val in enumerate(numbers):
            divisors = get_cached_divisors(val)
            if len(divisors) != n or len(set(divisors).intersection(set(all_divisors))) != 0:
                break
            all_divisors += divisors

        if len(all_divisors) == n ** 2:
            return numbers

cached_divisors = {}

print get_consecutive(4)


# print get_divisors(644)
# print get_divisors(645)
# print get_divisors(646)


print time.time() - start_time, "seconds"
