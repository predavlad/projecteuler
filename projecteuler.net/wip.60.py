import time
import math

# not done yet, bad approach
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


def check_pair_set(prime_pair):
    global primes
    for i in prime_pair:
        for j in prime_pair:
            if i != j:
                a, b = int(str(i) + str(j)), int(str(j) + str(i))
                if not is_prime(a) or not is_prime(b):
                    return False
    return True


limit = 1000000
primes = get_primes(limit)
primes.pop(0)  # remove the prime 2
prime_len = len(primes)
# sets found under 1000:
# [3, 7, 109, 673] # given in the problem
# [23, 311, 677, 827]
#
set_4 = [23, 311, 677, 827]

assert check_pair_set(set_4)

for i in primes:
    if i in set_4:
        continue
    if check_pair_set([23, 311, 677, 827, i]):
        print i
        break
# counter = 0
# for i in range(prime_len):
#     for j in range(i + 1, prime_len):
#         for k in range(j + 1, prime_len):
#             for l in range(k + 1, prime_len):
#             #     for m in range(l + 1, prime_len):
#                 prime_list = [primes[i], primes[j], primes[k], primes[l]]
#                 counter += 1
#                 if counter % 1000000 == 0:
#                     print "Checked", counter, 'pairs.'
#                 if check_pair_set(prime_list):
#                     print prime_list
#                     break

print "Finished."

print time.time() - start_time, "seconds"
