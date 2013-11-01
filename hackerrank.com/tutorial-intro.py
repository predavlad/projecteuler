V = 4
n = 6
ar = map(int, "1 4 5 7 9 12".split(' '))

for i in xrange(len(ar)):
    if V <= ar[i]:
        print i
        break
