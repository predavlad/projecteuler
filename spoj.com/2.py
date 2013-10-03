import time

start_time = time.time()


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


t = get_primes(1000000000)
print len(t)

test_cases = int(raw_input())
cases = []
for i in range(test_cases):
    cases.append(map(int, raw_input().split(' ')))

for n in cases:
    primes = get_primes(n[1])
    for p in primes:
        if p < n[0]:
            continue
        print p
    print

print time.time() - start_time, "seconds"