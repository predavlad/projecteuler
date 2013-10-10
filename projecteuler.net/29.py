import time

# 0.016 seconds
start_time = time.time()


def generate_squares(start, end):
    squares = set()
    for i in xrange(start, end + 1):
        for j in xrange(start, end + 1):
            squares.add(i ** j)
    return squares

print len(generate_squares(2, 100))

print time.time() - start_time, "seconds"
