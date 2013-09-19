length = 101

squaresSum = 0
for i in range(1, length):
    squaresSum += (i ** 2)


sumSquares = 0
for i in range(1, length):
    sumSquares += i

sumSquares = sumSquares * sumSquares

print sumSquares - squaresSum
