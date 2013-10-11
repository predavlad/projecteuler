import time
import math

# 6.7 seconds
start_time = time.time()


def is_pentagonal(n):
    """
     Necessary condition:
         (1 + 24n) is a perfect square
         sqrt(1 + 24n) = 5 mod 6
    """
    root = math.sqrt(1 + 24 * n)
    return True if root == math.trunc(root) and root % 6 == 5 else False


def get_diff(n1, n2):
    if is_pentagonal(abs(n1-n2)) and is_pentagonal(n1 + n2):
        return abs(n1 - n2)
    return False


pentagonal = [n * (3 * n - 1) / 2 for n in range(1, 3000)]
minim = 10 ** 10
vals = []

for i in pentagonal:
    for j in pentagonal:
        rez = get_diff(i, j)
        if rez:
            if minim > rez:
                vals = [i, j]
                minim = rez



print vals
print minim

print time.time() - start_time, "seconds"
