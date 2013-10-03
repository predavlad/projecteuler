import time
start_time = time.time()


def get_max_remainder(a):
    # thank you math !!!
    return 2 * a * ((a - 1) / 2)


MIN_A = 3
MAX_A = 1001
remainder = [0] * 1001

for a in range(MIN_A, MAX_A):
    rem = get_max_remainder(a)
    remainder[a] = rem

assert remainder[7] == 42

# print remainder
print sum(remainder)


print time.time() - start_time, "seconds"
