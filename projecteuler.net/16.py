# sum
digits = str(2 ** 1000)
sum = 0

for i in range(len(digits)):
    sum += int(digits[i])

print sum

# print map(int, str(2 ** 15).split()))


