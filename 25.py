import time

start_time = time.time()

f1, f2 = 1, 1
counter = 2

while len(str(f2)) < 1000:
    f2, f1 = f1, f2
    f2 += f1
    counter += 1
    # print counter, ': ', f1, f2

print counter

print time.time() - start_time, "seconds"