import time

start_time = time.time()


def check_palindrome(nr):
    return str(nr) == str(nr)[::-1]


def find_palindromes(length):
    inf = int('1' + '0' * (length - 1))
    sup = inf * 10
    for i in xrange(sup, inf, -1):
        for j in xrange(sup, i, -1):
            nr = i * j
            if check_palindrome(nr):
                yield nr


print max([i for i in find_palindromes(3)])

print time.time() - start_time, "seconds"
