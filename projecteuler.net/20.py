import time
from operator import mul

# 0.0 seconds
start_time = time.time()

product = str(reduce(mul, xrange(2, 101)))
print sum([int(product[i]) for i in range(0, len(product))])


print time.time() - start_time, "seconds"
