import time
import itertools

# 0.2 seconds
start_time = time.time()


counter = 0
for i in itertools.permutations(range(0, 10)):
    counter += 1
    if counter == 1000000:
        print counter, i
        break


print time.time() - start_time, "seconds"
