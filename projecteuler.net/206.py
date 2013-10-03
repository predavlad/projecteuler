import time
import math

# run time ~14 seconds
start_time = time.time()


def check_digits(n):
    n = str(n)
    for i in range(10):
        if n[2 * i] != str((i + 1) % 10):
            return False
    return True


assert check_digits('1_2_3_4_5_6_7_8_9_0')
assert not check_digits(13890191)
# print 13890191 * 13890191


SQUARE_LEN = 16  # add 900 at the end
min_square = 1020304050607080900
max_square = 1929394959697989999

# last 3 digits of square are 900, this means that the number must end in 30 or 70
min_nr = int(math.floor(math.sqrt(min_square))) // 100
max_nr = int(math.ceil(math.sqrt(max_square))) // 100

for i in range(min_nr, max_nr):
    n1 = int(str(i) + '30') ** 2
    n2 = int(str(i) + '70') ** 2
    if check_digits(n1):
        print n1, int(math.sqrt(n1))
        break
    if check_digits(n2):
        print n2, int(math.sqrt(n2))
        break


print time.time() - start_time, "seconds"
