import time

# 0.04 seconds
start_time = time.time()

number = 28433
power = 7830457
lim = 10 ** 10
no_lim = 1000

while power > 0:
    if power > no_lim:
        number *= 2 ** no_lim
        power -= no_lim
    elif power > 0:
        number *= 2
        power -= 1
    number %= lim


print number + 1

print time.time() - start_time, "seconds"
