import time
# 0.4 seconds
start_time = time.time()


def is_digit_fact(n):
    global facts
    return n == sum([facts[int(i)] for i in str(n)])


# generate the digit factorials that will be used
facts = {}
fact = lambda x: 1 if x == 0 else x * fact(x - 1)
for i in range(10):
    facts[i] = fact(i)


rez = [i for i in xrange(3, 10 ** 5) if is_digit_fact(i)]
print sum(rez)

print time.time() - start_time, "seconds"
