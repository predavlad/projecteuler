import time
import math

start_time = time.time()

txt = open('base_exp.txt').read().split("\n")
max_line = 0
current_line = 0
max_value = 0

for pair in txt:
    current_line += 1
    n, power = map(int, pair.split(','))
    temp = power * math.log(n)
    if temp > max_value:
        max_value = temp
        max_line = current_line


print max_line


print time.time() - start_time, 'seconds'
