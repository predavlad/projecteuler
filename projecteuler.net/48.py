import time

# 0.03 seconds
start_time = time.time()

power_sum = 0
for i in xrange(1, 1001):
    if i % 10 == 0:
        continue
    power_sum += i ** i
    power_sum %= 10 ** 10

print power_sum


print time.time() - start_time, "seconds"
