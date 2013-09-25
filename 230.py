import time

start_time = time.time()

g = 1.6180339887498949  # golden ratio

t = (
    '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679',
    '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
)

length = len(t[0])


def D(n):
    global length
    digit = (n - 1) % length
    j = (n - 1) // length
    print i, j
    k = 1 if j - 1 <= j // g * g < j else 0  # magic
    return int(t[k][digit])


print sum([10 ** i * D((127 + 19 * i) * 7 ** i) for i in range(18)])

print time.time() - start_time, "seconds"
