import time
from fractions import Fraction

# 0.6 seconds
start_time = time.time()


LIMIT = 1000
fract = Fraction(1, 2)
numbers = []
counter = 0

for i in range(LIMIT):
    fract = Fraction(1, Fraction(2) + fract)
    current_fract = Fraction(1) + fract

    if len(str(current_fract.numerator)) > len(str(current_fract.denominator)):
        numbers.append(current_fract)
        counter += 1

# print "Fraction #%d: %s" % (i + 2, Fraction(1) + fract)
print counter
# print numbers


print 'Seconds', time.time() - start_time
