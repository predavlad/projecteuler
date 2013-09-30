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


def smallest_multiple(nr):
    all_divisors = {}
    for i in range(2, nr):
        divisors = get_divisors(i)
        for key in divisors:
            if key in all_divisors:
                if divisors[key] > all_divisors[key]:
                    all_divisors[key] = divisors[key]
            else:
                all_divisors[key] = divisors[key]
    return all_divisors


all_divisors = smallest_multiple(20)

product = 1
for key in all_divisors:
    product *= key ** all_divisors[key]

print product
