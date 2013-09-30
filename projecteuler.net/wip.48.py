import time

start_time = time.time()

power_sum = 0
for i in range(1, 1001):
    if i % 10 == 0:
        continue
    power_sum += i ** i
    power_sum %= 10000000000

print power_sum


print time.time() - start_time, "seconds"
