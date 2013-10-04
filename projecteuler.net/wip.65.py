import math

class Fraction:
    """ Adition of fractions """
    numerator = 0
    denominator = 0

    def __init__(self, n, d=1):
        if type(d) != int:
            self.numerator = n * d.denominator + d.numerator
            self.denominator = d.numerator
        else:
            self.numerator = n
            self.denominator = d

    def smallest_multiple(self, x, y):
        i = 2
        multiple = 1
        while multiple % x != 0 or multiple % y != 0:
            temp_i = i
            while x % temp_i == 0 or y % temp_i == 0:
                temp_i *= i
            temp_i /= i
            multiple *= temp_i
            i += 1
        return multiple

    def __add__(self, other):
        assert other.__class__ == Fraction
        new_denominator = self.smallest_multiple(self.denominator, other.denominator)
        new_numerator = self.numerator * new_denominator / self.denominator
        new_numerator += other.numerator * new_denominator / other.denominator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)


def get_2(n):
    global e
    if n == 0:
        return Fraction(1)
    return Fraction(1, Fraction(2) + get_2(n - 1))


def get_e(n):
    global e
    if n == 0:
        return Fraction(2)
    print n, e[n]
    return Fraction(1, Fraction(e[n]) + get_e(n - 1))


e = []
starter = 2
for i in range(1, 101):
    e.append(1)
    e.append(2*i)
    e.append(1)

print e


print get_2(3)

print get_e(2)


# a = Fraction(1, 2)
# b = Fraction(1)
# c = a + b
# print c
