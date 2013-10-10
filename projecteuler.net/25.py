import time

# 0.14 seconds
start_time = time.time()

f1, f2, counter = 1, 1, 2
while len(str(f2)) < 1000:
    f2, f1 = f1 + f2, f2
    counter += 1

print counter

print time.time() - start_time, "seconds"
