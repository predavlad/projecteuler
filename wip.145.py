import time

start_time = time.time()


def is_reversible(n):
    rev = int(str(n)[::-1])
    s = rev + n
    for l in str(s):
        if int(l) % 2 == 0:
            return False
    return True


LIMIT = 10 ** 9

counter = 0
for i in range(1, LIMIT, 2):
    if int(str(i)[0]) % 2 != 0:
        continue
    if is_reversible(i):
        counter += 1

print counter * 2

print time.time() - start_time, "seconds"
