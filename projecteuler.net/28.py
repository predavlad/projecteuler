import time
import math

# 0.001 seconds
start_time = time.time()


size = 1001
total, i, increment = 0, 1, 2

while i <= size ** 2:
    if increment + 1 == math.sqrt(i):
        increment += 2
    total += i
    i += increment

print total


print time.time() - start_time, "seconds"
