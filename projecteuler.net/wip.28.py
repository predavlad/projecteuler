import time
import math

start_time = time.time()


def print_matrix(matrix):
    for i in range(len(matrix)):
        print matrix[i]
    print '=== END ==='

size = 5
matrix = [[0 for col in range(size)] for row in range(size)]

done = False
x, y = 2, 2
matrix[x][y] = 1
iteration = 3  # starting from an array of size 2, +2 per iteration
current = 1
half = x / 2

print_matrix(matrix)

while not done:

    for i in range(y + 1, iteration + 1):
        y = i
        current += 1
        matrix[x][y] = current

    for i in range(x + 1, iteration + 1):
        x = i
        current += 1
        matrix[x][y] = current

    for i in range(y - 1, iteration / 2 - 1, -1):
        y = i
        current += 1
        matrix[x][y] = current

    for i in range(x - 1, iteration / 2 - 1, -1):
        x = i
        current += 1
        matrix[x][y] = current

    iteration += 2

    print_matrix(matrix)

    if iteration == 6:
        break


print time.time() - start_time, "seconds"
