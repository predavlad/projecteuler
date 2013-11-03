import time

# 0.07 seconds
start_time = time.time()


def digit_sum(n):
    return sum([int(j) for j in str(n)])


def digit_power_sum(n, power):
    p = n ** power
    if digit_sum(p) == n:
        return True
    return False


POWERS = 9
MAX_DIGIT_SUM = 1000
rez = []
counter = 0

for i in range(2, MAX_DIGIT_SUM):
    for p in range(2, POWERS):
        if digit_power_sum(i, p):
            counter += 1
            rez.append(i ** p)

rez = sorted(rez)
print rez[29]

print time.time() - start_time, "seconds"
