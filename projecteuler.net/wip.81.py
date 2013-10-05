import time

start_time = time.time()

matrix = [map(int, i.split(',')) for i in open('matrix.txt').read().split('\n') if i != '']

SIZE = len(matrix)



print 'Seconds', time.time() - start_time
