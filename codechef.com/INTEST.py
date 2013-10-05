n, k = raw_input().split(' ')
n, k = int(n), int(k)
counter = 0
for i in xrange(n):
    t = input()
    if t % k == 0:
        counter += 1

print counter
