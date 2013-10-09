import time

start_time = time.time()


def fib(lim):
    a = b = 1
    while b < lim:
        yield b
        a, b = b, a + b


print sum([i for i in fib(4000000) if i % 2 == 0])


print time.time() - start_time, "seconds"
