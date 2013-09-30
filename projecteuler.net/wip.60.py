import time
import math

# very ugly solution, I didn't wait for it to finish, but the script
# only found 1 solution, and fairly quickly
# I assumed that the prime numbers would be less than 10.000, and apparently I was right
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
    global primes, pairs
    for i in prime_pair:
        for j in prime_pair:
            if i != j:
                a, b = int(str(i) + str(j)), int(str(j) + str(i))
                dict_check = str(min(a, b)) + '-' + str(max(a, b))
                if dict_check not in pairs:
                    if not is_prime(a) or not is_prime(b):
                        return False
                    else:
                        pairs[dict_check] = True
    return True


limit = 10000
primes = get_primes(limit)
primes.pop(0)  # remove the prime 2
prime_len = len(primes)
pairs = {}

counter = 0
for i in range(prime_len):
    for j in range(i + 1, prime_len):
        if not check_pair_set([primes[i], primes[j]]):
            continue
        for k in range(j + 1, prime_len):
            if not check_pair_set([primes[i], primes[j], primes[k]]):
                continue
            for l in range(k + 1, prime_len):
                if not check_pair_set([primes[i], primes[j], primes[k], primes[l]]):
                    continue
                for m in range(l + 1, prime_len):
                    prime_list = [primes[i], primes[j], primes[k], primes[l], primes[m]]
                    counter += 1
                    if counter % 1000000 == 0:
                        print "Checked", counter, 'pairs.'
                    if check_pair_set(prime_list):
                        print prime_list

print "Finished."

print time.time() - start_time, "seconds"
