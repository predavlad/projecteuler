import time

start_time = time.time()


def divisor_sum(n):
    """
    Get the sum of divisors of a number
    """
    global divisor_cache
    if n in divisor_cache:
        return divisor_cache[n]
    divisor_cache[n] = sum(get_divisors(n))
    return divisor_cache[n]


def get_divisors(n):
    """
    Get all the divisors of a number (including 1, but excluding the number)
    """
    yield 1
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            yield n / i


def perfect_number(n):
    """
    Check if n is a perfect number
    """
    return divisor_sum(n) == n


def number_chain(n):
    """
    Calculate the amicable chain of a number
    """
    if perfect_number(n):
        return 1
    new_n, counter = divisor_sum(n), 1
    chain = set()
    chain.add(n)
    chain_len = 1
    while new_n not in chain:
        chain.add(new_n)
        new_n = divisor_sum(new_n)
        chain_len += 1




divisor_cache, chain_cache = {}, {}

print number_chain(10)

print divisor_sum(28)

print time.time() - start_time, "seconds"
