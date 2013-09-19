import math

def is_prime(nr):
        limit = int(math.ceil(math.sqrt(nr)))
	for i in range(2, limit):
		if nr % i == 0:
			return False
	return True


def prime_factor(nr):
	max = 1
	limit = int(math.sqrt(nr))

	for i in range(2, limit):
		if nr % i == 0:
			if is_prime(i):
				print i
				max = i

	return max

print prime_factor(600851475143)	
