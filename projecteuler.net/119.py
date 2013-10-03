import time
# quite pleased with the result, 0.05 seconds
start_time = time.time()


def digit_sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s


def digit_power_sum(n, power):
    p = n ** power
    if digit_sum(p) == n:
        return True
    return False


POWERS = 9
MAX_DIGIT_SUM = 1000

assert digit_power_sum(8, 3)
assert digit_sum(512) == 8
rez = []
counter = 0
for i in range(2, MAX_DIGIT_SUM):
    for p in range(2, POWERS):
        if digit_power_sum(i, p):
            counter += 1
            # print i, '**', p, '=', i ** p
            rez.append(i ** p)

rez = sorted(rez)
print rez[29]

print time.time() - start_time, "seconds"
