import time

# 110 seconds
start_time = time.time()


def is_reversible(n):
    """
    Check if a number is reversible
    """
    s = n + int(str(n)[::-1])
    for l in str(s):
        if int(l) % 2 == 0:
            return False
    return True


# this will be enough, since 10 ** 9 gives no solutions
lim = 10 ** 8

counter = 0
for i in xrange(1, lim, 2):
    if int(str(i)[0]) % 2 != 0:
        continue
    if is_reversible(i):
        counter += 1
        if counter % 10000 == 0:
            print 'Found %d numbers checked until %d' % (counter, i)


print counter * 2

print time.time() - start_time, "seconds"
