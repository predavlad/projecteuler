import time

# 0.001 seconds
start_time = time.time()

f1 = f2 = counter = 1

fib = {1: 1}
for i in xrange(1001):
    f2, f1 = f1, f2
    f2 += f1
    counter += 1
    fib[counter] = f1


for i in range(1, 16):
    print "Golden nugget #" + str(i), 'solution: ',  fib[2*i] * fib[2*i + 1]

print time.time() - start_time, "seconds"
