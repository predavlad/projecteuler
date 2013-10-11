import time
from operator import mul

# 0.07 seconds
start_time = time.time()

removed, searched = 0, 1
fraction, d = '', {}

for i in xrange(1, 10000001):
    fraction += str(i)
    if len(fraction) >= searched:
        d[searched] = fraction[searched - 1]
        if searched == 1000000:
            break
        searched *= 10


print reduce(mul, [int(d[i]) for i in d])



print time.time() - start_time, "seconds"

