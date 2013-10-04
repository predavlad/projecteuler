import time
import math

# 0.01 seconds
start_time = time.time()


SIZE = 1001

i = 1
total = 0
increment = 2

while i <= SIZE ** 2:
    if increment + 1 == math.sqrt(i):
        increment += 2
    total += i
    i += increment

print total



print time.time() - start_time, "seconds"
