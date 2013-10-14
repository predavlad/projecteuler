import time

# 0.1 seconds
start_time = time.time()


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def next_iteration(n):
    return n + int(str(n)[::-1])


def is_lycrel(n):
    """
    Check if a number is a lycrel number.
    """
    counter = 1
    n = next_iteration(n)
    while not is_palindrome(n):
        n = next_iteration(n)
        counter += 1
        if counter > 50:
            return True
    return False


assert not is_lycrel(47)
assert not is_lycrel(349)
assert is_lycrel(10677)
assert next_iteration(349) == 1292
assert is_palindrome(next_iteration(47))


l = [i for i in range(1, 10001) if is_lycrel(i)]
print len(l)


print time.time() - start_time, "seconds"
