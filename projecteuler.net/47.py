import time
from collections import deque

# 0.37 seconds
start_time = time.time()


def count_divisors(n):
    """
    Count the prime divisors for all the numbers below n
    """
    div = [0] * n
    for i in xrange(2, n):
        if div[i] == 0:
            yield i, 1
            for j in xrange(i, n, i):
                div[j] += 1
        else:
            yield i, div[i]


cons = 4
prev = deque([0] * cons)
for number, divisors in count_divisors(10 ** 6):
    prev.popleft()
    prev.append(divisors)
    if sum(prev) == cons ** 2:
        print "First number in sequence: %d" % (number - cons + 1)
        break


print time.time() - start_time, "seconds"



