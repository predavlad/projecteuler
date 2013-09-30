import random
import time

# 4 second run time
start_time = time.time()


def next_iteration(nr, step_no):
    if nr % 2 == 0:
        return nr / 2, step_no + 1
    else:
        return 3 * nr + 1, step_no + 1


def get_steps(nr):

    global cache, max_sequence, max_seed

    if random.random() * 10000 < 1:
        print nr

    temp = nr
    step = 1

    while temp != 1:
        # print temp, step

        if temp in cache:
            step += (cache[temp] - 1)
            # print "Cached: #", temp, " - ", cache[temp]
            # print temp, step, cache[temp]
            break

        temp, step = next_iteration(temp, step)

    # print "===== DONE ====="
    if max_sequence < step:
        max_sequence = step
        max_seed = nr
    cache[nr] = step


max_seed = 0
max_sequence = 0
cache = {1: 4, 2: 2}

current = 3
longest = 0
limit = 1000000

for i in range(current, limit):
    get_steps(i)

print "Max Sequence is:"
print max_sequence, " from number: ", max_seed
# print cache

print time.time() - start_time, "seconds"
