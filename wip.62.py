import time
from itertools import permutations

# 2 minutes
start_time = time.time()

def is_permutation(a, b):
    if a == b:
        return False
    a = list(str(a))
    b = str(b)
    while a:
        letter = a.pop()
        b = b.replace(letter, '', 1)

    if len(b) == 0:
        return True
    return False


# def get_permutations(n):
#     nr = list(str(n))
#     perms = [i for i in permutations(nr)]
#     rez = []
#     for perm in perms:
#         rez.append(''.join(perm))
#     return map(int, rez)
#
#
def is_cube(nr):
    return pow(nr, 1.0 / 3) == int(pow(nr, 1.0 / 3))
#
#
# def is_perm_cubes(n, limit):
#     perms = get_permutations(n)
#     print perms
#     cubes = 0
#     for perm in perms:
#         if is_cube(perm):
#             cubes += 1
#     if cubes == limit:
#         return True
#     return False


def get_max_perm(n):
    n = ''.join(sorted(list(str(n)[::-1]), reverse=True))
    return int(n)


def get_min_perm(n):
    n = ''.join(sorted(list(str(n)[::-1]), reverse=False))
    return int(n)

assert get_max_perm(345) == 543


limit = 5
cubes = range(500, 5500)
perms = {}

for i in range(len(cubes)):
    for j in range(i, len(cubes)):
        cube_i = cubes[i] ** 3
        cube_j = cubes[j] ** 3
        if is_permutation(cube_i, cube_j):
            max_perm = get_max_perm(cube_i)
            if max_perm in perms:
                if cube_i not in perms[max_perm]:
                    perms[max_perm].append(cube_i)
                if cube_j not in perms[max_perm]:
                    perms[max_perm].append(cube_j)
            else:
                perms[max_perm] = [cube_i, cube_j]
            if len(perms[max_perm]) == limit:
                print get_min_perm(cube_i)
                print perms
                break

print '=== Done ==='

print perms


























#
#
#
#
#
# assert is_cube(27)
# assert not is_cube(20)
#
# number = 10000
# while not is_perm_cubes(number):
#     print number
#     number += 1
#
# print number


print time.time() - start_time, "seconds"
