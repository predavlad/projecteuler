import time

start_time = time.time()

length = 101

squaresSum = sum([i ** 2 for i in xrange(length)])
sumSquared = sum([i for i in xrange(length)]) ** 2

print sumSquared - squaresSum

print time.time() - start_time, "seconds"
