import time
from fractions import Fraction

start_time = time.time()

LIMIT = 4
numbers = []
counter = 0

e = []
for i in range(1, LIMIT):
    e.append(1)
    e.append(2*i)
    e.append(1)

print e
fract = Fraction(1, e[LIMIT - 1])
for i in range(LIMIT-2, 0, -1):
    fract = Fraction(1, Fraction(e[i]) + fract)
    current_fract = Fraction(2) + fract
    print i, current_fract


# print "Fraction #%d: %s" % (i + 2, Fraction(1) + fract)
print counter
# print numbers


print 'Seconds', time.time() - start_time
