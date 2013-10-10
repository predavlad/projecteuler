import time
import math

# 0.13 seconds
start_time = time.time()


def proper_divisors(n):
    """
    Get the proper divisors from a number
    """
    yield 1
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if i != n / i:
                yield n / i


def is_abundant(n):
    """
    Calculates if n is abundant (the sum of its proper divisors is larger than the number)
    """
    if n % 2 != 0 and n % 3 != 0:
        return False
    return sum(proper_divisors(n)) > n


def is_abundant_sum(n):
    """
    at this stage, n is odd (and over 48). This means that we need to write it
    as the sum of an odd + even abundant number
    since there are fewer odd numbers, this is the way to do it
    """
    global odd_abundant, even_abundant
    for i in odd_abundant:
        if i > n:
            continue
        if (n - i) in abundant:
            return True

    return False


# set up initial values we will need later on
abundant_under_49 = [24, 30, 32, 36, 38, 40, 42, 44, 48]
non_abundant_sum = sum([i for i in xrange(1, 49) if i not in abundant_under_49])
abundant = set(i for i in xrange(1, 20162) if is_abundant(i))
odd_abundant = set(i for i in abundant if i % 2 == 1)

# this is the big loop that calculates everything
non_abundant_sum += sum([i for i in xrange(49, 20162, 2) if not is_abundant_sum(i)])


print non_abundant_sum

print time.time() - start_time, "seconds"
