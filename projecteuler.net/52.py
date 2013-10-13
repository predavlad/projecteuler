import time

# 2.3 seconds
start_time = time.time()


# check if 2 numbers are permutations of each other
def is_permutation(a, b):
    a, b = set(str(a)), set(str(b))
    return len(a & b) == len(a) == len(b)

max_check = 6
for i in xrange(1, 1000000):
    correct = True
    for j in xrange(max_check):
        if not is_permutation(i * (j + 1), i):
            correct = False
    if correct:
        print "Found: ", i
        break

print time.time() - start_time, "seconds"
