import time
from fractions import Fraction

# 0.65 seconds
start_time = time.time()


fract = Fraction(1, 2)
numbers, counter, lim = [], 0, 1000

for i in xrange(lim):
    fract = Fraction(1, Fraction(2) + fract)
    current_fract = Fraction(1) + fract

    if len(str(current_fract.numerator)) > len(str(current_fract.denominator)):
        numbers.append(current_fract)
        counter += 1

# print "Fraction #%d: %s" % (i + 2, Fraction(1) + fract)
print counter
# print numbers


print time.time() - start_time, 'seconds'
