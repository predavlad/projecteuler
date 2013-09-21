import time

start_time = time.time()


def is_pandigital(nr, n):
    nr = str(nr)
    beg = nr[0:n]
    end = nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True


assert is_pandigital(123456789, 9) is True
assert is_pandigital(956487123123123956487123, 9) is True
assert is_pandigital(1, 9) is False

f1, f2 = 1, 1
counter = 2
found = False

while not found:
    f2, f1 = f1, f2
    f2 += f1
    if is_pandigital(f2, 9):
        found = True
    counter += 1
    if counter % 500 == 0:
        print counter

print counter
print f2

print time.time() - start_time, "seconds"
