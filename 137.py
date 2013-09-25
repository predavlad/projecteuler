import time
import math

start_time = time.time()

f1, f2 = 1, 1
counter = 1

# populate the first few fibbonnacci numbers
fib = {1: 1}
for i in range(1001):
    f2, f1 = f1, f2
    f2 += f1
    counter += 1
    fib[counter] = f1


for i in range(1, 31):
    print "Golden nugger #" + str(i), 'solution: ',  fib[2*i] * fib[2*i + 1]

print time.time() - start_time, "seconds"
