import time

start_time = time.time()


matrix = map(lambda x: map(int, x.split(' ')), open('18.txt').read().split("\n"))

for i in xrange(len(matrix) - 2, -1, -1):
    for j in xrange(i, -1, -1):
        matrix[i][j] += max([matrix[i + 1][j], matrix[i + 1][j + 1]])


print matrix[0][0]

print time.time() - start_time, "seconds"

