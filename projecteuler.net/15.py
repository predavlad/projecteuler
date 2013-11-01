import time

# 0.0 seconds
start_time = time.time()
matrix, size = {}, 21


for i in xrange(size):
    if i not in matrix:
        matrix[i] = {}
    matrix[i][0], matrix[0][i] = 1, 1


for i in xrange(1, size):
    for j in xrange(1, size):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

print matrix[size - 1][size - 1]

print time.time() - start_time, "seconds"
