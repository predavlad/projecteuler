import time
import math

# 5 seconds
start_time = time.time()


# thank you math!
def is_pentagonal(n):
    # Necessary condition:
    #     (1 + 24n) is a perfect square
    # Required:
    #     sqrt(1 + 24n) = 5 mod 6
    root = math.sqrt(1 + 24 * n)
    return True if root == math.trunc(root) and root % 6 == 5 else False


def get_diff(n1, n2):
    if is_pentagonal(abs(n1-n2)) and is_pentagonal(n1 + n2):
        return abs(n1 - n2)
    return False


pentagonal = [n * (3 * n - 1) / 2 for n in range(1, 3000)]
minim = None
vals = []

for i in range(len(pentagonal)):
    for j in range(i, len(pentagonal)):
        rez = get_diff(pentagonal[i], pentagonal[j])
        if rez:
            if minim is None:
                minim = rez
            elif minim > rez:
                    vals = [pentagonal[i], pentagonal[j]]
                    minim = rez



print vals
print minim

print time.time() - start_time, "seconds"
