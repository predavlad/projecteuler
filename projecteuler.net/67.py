import time

# 0.008 seconds
start_time = time.time()


matrix = [i.split(' ') for i in open('67.txt').read().split("\n")]

for i in range(len(matrix) - 1, -1, -1):
    for j in range(i, -1, -1):
        matrix[i][j] = int(matrix[i][j])

for i in range(len(matrix) - 2, -1, -1):
    for j in range(i, -1, -1):
        nr_checked = [matrix[i + 1][j], matrix[i + 1][j + 1]]
        matrix[i][j] += max(nr_checked)

print matrix[0][0]

print time.time() - start_time, "seconds"

