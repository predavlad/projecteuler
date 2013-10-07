import time
import math

start_time = time.time()


def get_dist(a, b, c):
    return math.sqrt(a ** 2 + (b + c) ** 2)


squares = {}


print get_dist(6, 5, 3)


print time.time() - start_time, "seconds"
