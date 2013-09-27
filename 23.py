import time
import math

# run time - 2 seconds
start_time = time.time()
abundant_numbers = []
odd_abundant = []
even_abundant = []
good_numbers = []


def get_proper_divisors(n):
    divisors = []
    maxValue = int(math.sqrt(n)) + 1
    for i in range(1, maxValue):
        if n % i == 0:
            if i not in divisors:
                divisors.append(i)
                quotient = n / i
        if quotient == n:
            continue
        if quotient not in divisors:
            divisors.append(quotient)
    return divisors


def is_abundant_number(nr):
    if nr % 2 != 0 and nr % 3 != 0:
        return False
    return sum(get_proper_divisors(nr)) > nr


def check_abundant_sums(n):
    global odd_abundant, even_abundant

    # at this stage, n is odd (and over 48). This means that we need to write it
    # as the sum of an odd + even abundant number
    # since there are fewer odd numbers, this is the way to do it
    for i in odd_abundant:
        if i > n:
            break
        if (n - i) in even_abundant:
            return False

    return True


# 20161 is the last number that cannot be written as a sum of 2 abundant numbers
for i in range(1, 20162):
    if is_abundant_number(i):
        abundant_numbers.append(i)
        if i % 2 == 0:
            even_abundant.append(i)
        else:
            odd_abundant.append(i)


for i in range(1, 20162):
    if i <= 48:
        # these are the abundant numbers <= 48
        if i not in [24, 30, 32, 36, 38, 40, 42, 44, 48]:
            good_numbers.append(i)
    else:
        # even numbers over 48 are abundant
        if i % 2 != 0:
            if check_abundant_sums(i):
                good_numbers.append(i)


print len(good_numbers)  # how many numbers cannot be written as the sum of 2 abundant numbers
print good_numbers  # the list with numbers
print sum(good_numbers)  # the sum


print time.time() - start_time, "seconds"
