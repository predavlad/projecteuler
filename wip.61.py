import time

start_time = time.time()


def P(base, n):
    if base not in range(3, 9):
        raise Exception
    if base == 3:
        return n * (n+1) / 2
    if base == 4:
        return n * n
    if base == 5:
        return n * (3 * n - 1) / 2
    if base == 6:
        return n * (2 * n - 1)
    if base == 7:
        return n * (5 * n - 3) / 2
    if base == 8:
        return n * (3 * n - 2)


def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]


def get_next_number(n, ignored=[]):
    global numbers
    search = diff(range(3, 9), ignored)
    rez = []
    if len(search):
        for i in search:
            for j in numbers[i]:
                if j not in rez:
                    if str(n)[2:] == str(j)[:2]:
                        rez.append(j)
    return rez



assert P(3, 127) == 8128
assert P(4, 91) == 8281
assert P(5, 44) == 2882
assert P(6, 5) == 45
assert P(7, 5) == 55
assert P(8, 5) == 65

# get all the 4 digits numbers
numbers = {}
for i in range(3, 9):
    numbers[i] = [P(i, j) for j in range(1, 145) if len(str(P(i, j))) == 4 and '0' not in str(P(i, j))]



for i in range(3, 9):
    for j in numbers[i]:
        if len(get_next_number(j, [i])) == 0:
            numbers[i].remove(j)

p = 1
for i in range(3, 9):
    print numbers[i]
    p *= len(numbers[i])
print p


print time.time() - start_time, "seconds"

