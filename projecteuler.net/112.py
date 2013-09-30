import time
import math

# about 24 seconds run time
start_time = time.time()

def is_bouncy(n):
    if n < 100:
        return False
    n = str(n)
    is_asc = True
    is_desc = True
    for i in range(1, len(str(n))):
        if int(n[i - 1]) > int(n[i]):
            is_asc = False
        if int(n[i - 1]) < int(n[i]):
            is_desc = False
    if is_asc or is_desc:
        return False
    return True


assert is_bouncy(525)
assert not is_bouncy(134468)
assert is_bouncy(155349)

bouncy_count = 0
not_bouncy_count = 0

for i in range(1, 10000000):
    if is_bouncy(i):
        bouncy_count += 1
    else:
        not_bouncy_count += 1
    ratio = bouncy_count / float(not_bouncy_count + bouncy_count)
    if ratio > 0.9899:
        print i, ratio
    if ratio > 0.99:
        break

print ratio

#print bouncy_count, not_bouncy_count, bouncy_count / float(not_bouncy_count + bouncy_count)


print time.time() - start_time, 'seconds'
