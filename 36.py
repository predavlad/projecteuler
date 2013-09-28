import time

start_time = time.time()


def check_palindrome(nr):
    return str(nr) == str(nr)[::-1]


def is_double_base_palindrome(nr):
    if not check_palindrome(nr):
        return False

    bin_nr = str(bin(nr)).replace('0b', '')
    if not check_palindrome(bin_nr):
        return False

    return True


rez = []
for i in range(1, 1000000):
    if is_double_base_palindrome(i):
        rez.append(i)


print rez
print len(rez)
print sum(rez)

print time.time() - start_time, "seconds"
