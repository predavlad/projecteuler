import time
import math

# 1.5 seconds
start_time = time.time()

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


limit = 1000000
primes = get_primes(limit)
print 'There are', len(primes), 'primes that we will check.'
max_seq = 0
max_seq_nr = 0

# j is the index of the prime from which we will start looking
# no point in setting the starting point higher than this
for j in range(0, int(math.sqrt(len(primes)))):
    prime_sum = 0
    prime_count = 0

    if max_seq > len(primes[j:]):
        break
    for i in primes[j:]:
        # print i, prime_sum
        if prime_sum < limit:
            prime_sum += i
            prime_count += 1
            if prime_count > max_seq:
                if is_prime(prime_sum):
                    max_seq = prime_count
                    max_seq_nr = prime_sum
        else:
            break

# print prime_sum
print max_seq, max_seq_nr


print time.time() - start_time, "seconds"
