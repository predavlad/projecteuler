import time

# brute force FTW! 4 seconds
start_time = time.time()

## optimized for this exercise
def is_pandigital(nr, n):
    nr = str(nr)
    #beg = nr[0:n]
    #end = nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in nr:  # beg or i not in end:
            return False
    return True


def is_pandigital_multiple(n, div_list):
    new_nr = ''
    for i in range(len(div_list)):
        new_nr += str(int(div_list[i]) * n)

    if len(new_nr) != 9:
        return False

    if is_pandigital(new_nr, 9):
        return new_nr

    return False


assert is_pandigital_multiple(192, range(1, 4))
assert is_pandigital_multiple(9, range(1, 6))

n = 5
max_pandigital_multiple = 0

for i in range(1, 50000):
    for j in range(2, 16):
        rez = is_pandigital_multiple(i, range(1, j + 1))
        if rez:
            if max_pandigital_multiple < rez:
                max_pandigital_multiple = rez

print max_pandigital_multiple

print time.time() - start_time, "seconds"
