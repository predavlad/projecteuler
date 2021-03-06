import time

# 4 seconds
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


size = 30001
size_sq = size ** 2
counter, i, prime_no, increment = 1, 1, 0, 2
debug_str = "Checked %d numbers on diagonals, found %d primes, square area %d, ratio %f"

while i <= size_sq:
    if (increment + 1) ** 2 == i:
        ratio = round(prime_no / float(counter) * 100, 6)
        if ratio < 10.0:
            print debug_str % (counter, prime_no, increment+1, ratio)
            break
        increment += 2
    counter += 1
    if is_prime(i):
        prime_no += 1
    i += increment

print "Ratio found: %f for square length %d" % (ratio, increment + 1)

print time.time() - start_time, "seconds"
