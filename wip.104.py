import time

start_time = time.time()


def is_pandigital(nr):
    digits = "123456789"
    nr = str(nr)
    for i in digits:
        if str(i) not in nr[0:9]:
            return False
        if str(i) not in nr[-9:]:
            return False

    return True


f1, f2 = 1, 1
counter = 2
found = False

while not found:
    f2, f1 = f1, f2
    f2 += f1
    if is_pandigital(f2):
        found = True
    counter += 1
    if counter % 500 == 0:
        print counter

print counter
print f2

print time.time() - start_time, "seconds"