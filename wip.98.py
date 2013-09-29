import time

start_time = time.time()

txt = open('98.txt').read().split(',')
print txt

print time.time() - start_time, 'seconds'
