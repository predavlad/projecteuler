import time

start_time = time.time()

counter = 0
for power in range(1, 25):
    for i in range(1, 100):
        n = i ** power
        if len(str(n)) == power:
            print str(i) + " ** " + str(power) + " = " + str(n)
            counter += 1

print counter

print time.time() - start_time, "seconds"
