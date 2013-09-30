import time
import math

# 6 seconds
start_time = time.time()


def is_prime(nr):
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True

max_seq = 0
max_a = 0
max_b = 0
for a in range (-1000, 1000):
    for b in range(2, 1000):
        n = 0
        nr = b
        while is_prime(nr):
            nr = n * n + n * a + b
            if nr <= 1:
                break
            n += 1

        if n > max_seq:
            print max_seq, ' - with numbers: ', a, b
            max_seq, max_a, max_b = n, a, b


print max_seq, max_a, max_b

print time.time() - start_time, "seconds"
