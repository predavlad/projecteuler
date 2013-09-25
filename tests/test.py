import time

start_time = time.time()


def digit_pos(n):
    return (127 + 19 * n) * (7 ** n)


def D(A, B, digit_searched):
    len_a, len_b = len(A), len(B)
    fib_lengths = {1: len_a, 2: len_b}
    counter = 2

    while len_b < digit_searched:
        counter += 1
        len_b, len_a = len_a, len_b
        len_b += len_a
        fib_lengths[counter] = len_b

    counter -= 1
    while digit_searched > len(A) or counter > 2:
        digit_searched = abs(fib_lengths[counter] - digit_searched)
        counter -= 1

    # print "Digit found in number #" + str(counter) + " digit #" + str(len(A) - digit_searched)
    if counter == 1:
        digit = str(A)
    else:
        digit = str(B)
    digit = digit[len(A) - digit_searched - 1]
    # print "Digit found: " + digit
    print fib_lengths
    return int(digit)


assert digit_pos(1) == 1022
assert digit_pos(2) == 8085
assert digit_pos(17) == 104683731294243150
assert D('1415926535', '8979323846', 35) == 9
assert D('1415926535', '8979323846', 36) == 2
assert D('1415926535', '8979323846', 49) == 4

f1 = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
f2 = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'

digit_sums = 0
for i in range(0, 18):
    print "Searching for digit #", digit_pos(i), "for n = " + str(i)
    digit = D(f1, f2, digit_pos(i))
    digit_sums += (10 ** i) * int(digit)

print digit_sums

print time.time() - start_time, "seconds"
