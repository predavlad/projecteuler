import time

# very ugly solution, I didn't wait for it to finish, but the script
# only found 1 solution, and fairly quickly
# I assumed that the prime numbers would be less than 10.000, and apparently I was right
# 10 seconds run time
start_time = time.time()


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: return False
        f += 6
    return True


def get_primes(n):
    """
    Get all the primes smaller than n
    """
    primes = [0] * n
    for i in xrange(2, n):
        if primes[i] == 0:
            yield i
        else:
            continue
        for j in xrange(1, n // i):
            primes[j * i] = 1


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


def solve():
    global limit, primes
    primes.pop(0)  # remove the prime 2
    prime_len = len(primes)

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
                            print sum(prime_list)
                            return


limit = 10000
primes = list(get_primes(limit))
pairs = {}

solve()


print "Finished."

print time.time() - start_time, "seconds"
