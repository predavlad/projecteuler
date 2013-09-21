import time

start_time = time.time()

def check_fraction(a, b):
    if b % 10 == 0 or b % 11 == 0 or (a / b) >= 1 or str(a)[1] != str(b)[0]:
        return False

    x = float(str(a)[0])
    y = float(str(b)[1])
    return x / y == a / b


def get_fractions():
    results = []
    for i in range(11, 100):
        for j in range(i, 100):
            if check_fraction(float(i), float(j)):
                results.append([i, j])
    return results

rez = get_fractions()
print rez
print len(rez)

print time.time() - start_time, "seconds"
