import time
import math

# 0.0.
start_time = time.time()

txt = [i.split(',') for i in open('99.txt').read().split("\n") if i != '']
max_value = current_line = max_line = 0

for pair in txt:
    n, power = int(pair[0]), int(pair[1])
    current_line += 1
    temp = power * math.log(n)
    if temp > max_value:
        max_value = temp
        max_line = current_line


print max_line


print time.time() - start_time, 'seconds'
