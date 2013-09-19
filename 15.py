import time

start_time = time.time()
matrix = {}

size = 21

def print_matrix(matrix):
    global size
    for i in range(size):
        print
        for j in range(size):
            print matrix[i][j],


for i in xrange(size):
    if i not in matrix:
        matrix[i] = {}
    matrix[i][0] = 1
    matrix[0][i] = 1

for i in range(1, size):
    for j in range(1, size):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

print_matrix(matrix)

print time.time() - start_time, "seconds"
