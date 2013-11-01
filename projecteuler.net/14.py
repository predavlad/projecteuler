import time

# 3.5 seconds
start_time = time.time()


def next_iteration(nr, step_no):
    if nr % 2 == 0:
        return nr / 2, step_no + 1
    else:
        return 3 * nr + 1, step_no + 1


def get_steps(n):
    global cache, max_sequence, max_seed
    temp, step = n, 1

    while temp != 1:
        if temp in cache:
            step += (cache[temp] - 1)
            break
        temp, step = next_iteration(temp, step)

    if max_sequence < step:
        max_sequence = step
        max_seed = n

    cache[n] = step


max_seed = max_sequence = longest = 0
cache = {1: 4, 2: 2}
current, limit = 3, 1000000

for i in range(current, limit):
    get_steps(i)


print "Max Sequence is:", max_sequence, " from number: ", max_seed

print time.time() - start_time, "seconds"
