import time

# 4 seconds
start_time = time.time()


# check if 2 numbers are permutations of each other
def is_permutation(a, b):
    a = list(str(a))
    b = str(b)
    while a:
        letter = a.pop()
        b = b.replace(letter, '', 1)

    if len(b) == 0:
        return True
    return False

max_check = 6
for i in range(1, 1000000):
    correct = True
    for j in range(max_check):
        if not is_permutation(i * (j + 1), i):
            correct = False
    if correct:
        print "Found: ", i
        break

print time.time() - start_time, "seconds"
