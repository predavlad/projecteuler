import time

# 0.3 seconds
start_time = time.time()


def is_palindrome(nr):
    return str(nr) == str(nr)[::-1]


def is_double_base_palindrome(n):
    return is_palindrome(n) and is_palindrome(str(bin(n)).replace('0b', ''))


print sum([i for i in xrange(1, 10**6, 2) if is_double_base_palindrome(i)])


print time.time() - start_time, "seconds"
