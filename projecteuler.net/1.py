import time

# 0.0 seconds
start_time = time.time()
print sum([i for i in range(1000) if not (i % 5 and i % 3)])


print time.time() - start_time, "seconds"
