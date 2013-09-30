import time

start_time = time.time()

fraction = ''
removed = 0
d = {}
searched = 1

for i in range(1, 10000001):
    fraction += str(i)
    if len(fraction) >= searched:
        d[searched] = fraction[searched - 1]
        if searched == 1000000:
            print 'STOP'
            break
        searched *= 10

p = 1
for i in d:
    p *= int(d[i])
print d
print len(d)
print p



print time.time() - start_time, "seconds"

