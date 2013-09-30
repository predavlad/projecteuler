import time

start_time = time.time()

def get_fact(nr):
    global fact_cache
    prod = 1
    for i in range(1, nr + 1):
        prod *= i
    return prod


# def get_perms(n, k):
#     if n + k not in fact_cache:
#         ret =
#     else:
#         ret = fact_cache[n + k]


    # def partition(number):
    # part_sum = 0
    # for i in range(number):
    #     if i in cache:
    #         part_sum += cache[i]
    #     else:
    #         part_sum += partition(i) * get_perms(number, i)
    # return part_sum


assert get_fact(3) == 6
assert get_fact(4) == 24


# cache = {0: 1, 1: 1, 2: 2, 3: 5}
# fact_cache = {}
# print partition(5)

print time.time() - start_time, "seconds"
