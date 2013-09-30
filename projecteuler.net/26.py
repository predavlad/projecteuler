import time
import math

start_time = time.time()

sequenceLen = 0

for i in range(1000, 1, -1):
    remainders = {}
    if sequenceLen > i:  # a sequence cannot be larger than the number we divide 1 to
        break

    val = 1
    remainders[i] = 0
    remainders[val] = 0
    pos = 0

    while remainders[val] == 0 and val != 0:
        remainders[val] = pos
        val *= 10
        val %= i
        pos += 1
        if val not in remainders:
            remainders[val] = 0

    if (pos - remainders[val]) > sequenceLen:
        sequenceLen = pos - remainders[val]


print sequenceLen

print time.time() - start_time, "seconds"
