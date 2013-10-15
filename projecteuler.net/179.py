import time

# 40 seconds. Not a great solution, but it's under 1 minute
# after it reaches 1% it speeds up exponentially
start_time = time.time()


def count_consecutive_divisors(n):
    """
    Counts all the numbers i between 2 and n for which the number of divisors of i
    is equal to the number of divisors of i + 1
    """
    divs = {}
    percent = n // 100
    for i in xrange(n):
        divs[i] = 2  # 1 and i

    prev = counter = 0
    for i in xrange(2, n):
        if i % percent == 0:
            print "%d percent" % (i // percent)

        for j in xrange(2 * i, n, i):
            divs[j] += 1

        if prev == divs[i]:
            counter += 1
        prev = divs[i]

    return counter

print count_consecutive_divisors(10 ** 7)


print time.time() - start_time, "seconds"
