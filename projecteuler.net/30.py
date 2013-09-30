import time

start_time = time.time()

def sum_digit_power(nr, power):
    if nr < 10:
        return False
    nr_str = str(nr)
    digit_sum = 0
    for i in range(len(nr_str)):
        digit_sum += int(nr_str[i]) ** power

    if digit_sum == nr:
        return True
    return False


nr = [i for i in range(1, 1000000) if sum_digit_power(i, 5)]
print nr
print len(nr)
print sum(nr)


assert sum_digit_power(1634, 4)
assert sum_digit_power(8208, 4)
assert not sum_digit_power(1, 4)

print time.time() - start_time, "seconds"
