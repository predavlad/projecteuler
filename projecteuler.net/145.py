import time

# crappy brute force solution. 111 seconds
start_time = time.time()


def is_reversible(n):
    rev = int(str(n)[::-1])
    s = rev + n
    for l in str(s):
        if int(l) % 2 == 0:
            return False
    return True


# this will be enough, since 10 ** 9 gives no solutions
LIMIT = 10 ** 8

counter = 0
for i in xrange(1, LIMIT, 2):
    if int(str(i)[0]) % 2 != 0:
        continue
    if is_reversible(i):
        counter += 1
        if counter % 10000 == 0:
            print 'Found %d numbers checked until %d' % (counter, i)


print counter * 2

print time.time() - start_time, "seconds"
