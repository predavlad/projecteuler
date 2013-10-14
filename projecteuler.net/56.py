import time

# 0.44 seconds
start_time = time.time()


def digit_sum(n):
    """
    Return the sum of the digits in number n
    """
    return sum(map(int, str(n)))


assert digit_sum(22) == 4
assert digit_sum(999) == 27

max_digit_sum = 0
for a in xrange(1, 100):
    for b in xrange(1, 100):
        max_digit_sum = max(max_digit_sum, digit_sum(a ** b))

print max_digit_sum

print time.time() - start_time, "seconds"
