import time

# 0.01
start_time = time.time()


def rectangle_sum(m, n):
    return m * n * (m+1) * (n+1) / 4


number = 2000000
min_dif = number
current = []

for i in range(1, 200):
    for j in range(i, 200):
        rect_sum = rectangle_sum(i, j)
        if min_dif > abs(number - rect_sum):
            min_dif = abs(number - rect_sum)
            current = [i, j]

print current
print rectangle_sum(current[0], current[1])
print current[0] * current[1]


print time.time() - start_time, "seconds"
