import time

# 2 seconds
start_time = time.time()


def strip_number(n):
    if len(str(n)) <= 10:
        return n
    else:
        return int(''.join(str(n)[-10:]))

number = 28433
power = 7830457

while power > 0:
    if power > 10:
        number *= 2 ** 10
        power -= 10
    elif power > 0:
        number *= 2
        power -= 1
    number = strip_number(number)

print number + 1

print time.time() - start_time, "seconds"
