import time

start_time = time.time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]
matrix, target = {}, 200

for y in xrange(0, target + 1):
    matrix[y, 0] = 1

for y in xrange(0, target + 1):
    print y, ":", 1,
    for x in xrange(1, len(coins)):
        matrix[y, x] = 0
        if y >= coins[x]:
            matrix[y, x] += matrix[y, x - 1]
            matrix[y, x] += matrix[y - coins[x], x]
        else:
            matrix[y, x] = matrix[y, x - 1]
        print matrix[y, x],
    print


print time.time() - start_time, "seconds"
