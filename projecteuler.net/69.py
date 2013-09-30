import time
import math

# run time - 2 seconds
start_time = time.time()


def is_prime(nr):
    if nr == 2:
        return True
    limit = int(math.ceil(math.sqrt(nr))) + 1
    for i in range(2, limit):
        if nr % i == 0:
            return False
    return True


def get_divisors(nr):
    divisors = {}
    for i in range(2, nr + 1):
        nrDiv = 0
        while nr % i == 0:
            nrDiv += 1
            nr /= i
        if nrDiv != 0:
            divisors[i] = nrDiv
    return divisors


def get_toilent_prime(prime):
    return len([i for i in range(1, prime) if prime % i != 0 or i == 1])


def get_toilent_all(n):
    global cached
    if is_prime(n):
        toilent_nr = get_toilent_prime(n)
        cached[n] = toilent_nr
        return toilent_nr
    divisors = get_divisors(n)
    toilent_nr = n
    for key in divisors.keys():
        toilent_nr *= ((float(key) - 1) / key)
    return int(toilent_nr)


cached = {}

assert get_toilent_all(2) == 1
assert get_toilent_all(3) == 2
assert get_toilent_all(4) == 2
assert get_toilent_all(5) == 4
assert get_toilent_all(6) == 2
assert get_toilent_all(7) == 6
assert get_toilent_all(8) == 4
assert get_toilent_all(9) == 6
assert get_toilent_all(10) == 4


### Works, but not actually efficient enough to brute force this
# max_ratio = 0.0
# for i in range(2, 10000):
#     toilent_nr = get_toilent_all(i)
#     ratio = i / float(toilent_nr)
#     if i % 1000 == 0:
#         print "got #", i
#     if ratio > max_ratio:
#         max_ratio = ratio
# print "Max ratio: ", max_ratio

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


primes = get_primes(200)
prod = 1
for i in primes:
    old_prod = prod
    prod *= i
    if prod > 1000000:
        print old_prod
        break







print time.time() - start_time, "seconds"
