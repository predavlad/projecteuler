def fib(limit):
	a = 1
	b = 1
	temp = sum = 0
	while b < limit:
		temp = a
		a = b
		b += temp
		if b % 2 == 0 and b < limit:
			print b
			sum += b

	return sum
		

print fib(4000000)
