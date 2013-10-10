import time

start_time = time.time()

# a one liner :P
print sum([int(i) for i in str(2 ** 1000)])


print time.time() - start_time, "seconds"
