import time

# 0.002 seconds
start_time = time.time()

sequenceLen = 0

for i in range(1000, 1, -1):
    remainders = {}
    if sequenceLen > i:  # a sequence cannot be larger than the number we divide 1 to
        break

    val = 1
    remainders[i] = remainders[val] = pos = 0

    while remainders[val] == 0 and val != 0:
        remainders[val], pos = pos, pos + 1
        val = (val * 10) % i
        if val not in remainders:
            remainders[val] = 0

    if (pos - remainders[val]) > sequenceLen:
        sequenceLen = pos - remainders[val] + 1


print sequenceLen

print time.time() - start_time, "seconds"
