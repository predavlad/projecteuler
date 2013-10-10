import time
import itertools
from operator import mul

# 1.5 seconds
start_time = time.time()


def sum_digit_power(n, power):
    """
    Calculates the sum of the digits in n at a giver power
    """
    return sum([int(i) ** power for i in str(n)])


lim = (9 ** 5) * 6  # let's say the numbers will contain a maximum of 6 digits
nr = [i for i in xrange(10, lim) if sum_digit_power(i, 5) == i]


print nr
print sum(nr)


assert sum_digit_power(1634, 4)
assert sum_digit_power(8208, 4)


##### Below is a pretty inefficient version (3.4 seconds)
##### But it  was an interesting idea and fun to write :)
# def perm(seq, n):
#     for p in itertools.product(seq, repeat=n):
#         yield p
#
# pow5 = {i: i ** 5 for i in range(10)}
# numbers = 0
# for i in perm(range(10), 6):
#     nr = sum([pow5[j] for j in i])
#     if nr == int(''.join(map(str, i))):
#         numbers += nr
#
# print numbers - 1 # we counted the number 1 wrongly


print time.time() - start_time, "seconds"
