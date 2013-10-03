import time

start_time = time.time()

def print_r(n):
    for i in n:
        print n[i]


def remove_first_digit(num):
    return int(str(num)[1:])


def remove_last_digit(num):
    return int(str(num)[:2])


def compatible_digits(a, b):
    a = str(a)
    b = str(b)
    if a[0] == b[2] or len(set(a)) != 3 or len(set(b)) != 3:
        return False
    return True

def pand_merge(a, b):
    return []


primes = [2, 3, 5, 7, 11, 13, 17]
numbers = {}
nums = {}
for i in range(len(primes)):
    nums[primes[i]] = {}
    numbers[primes[i]] = [{'n': j, 'first': remove_last_digit(j), 'last': remove_first_digit(j)}
                          for j in range(100, 1000) if j % primes[i] == 0]


for i in range(len(primes) - 1):
    for x in numbers[primes[i]]:
        for y in numbers[primes[i + 1]]:
            if x['last'] == y['first']:
                if not compatible_digits(x['n'], y['n']):
                    continue

                if x['n'] not in nums[primes[i]]:
                    nums[primes[i]][x['n']] = []
                nums[primes[i]][x['n']].append(y['n'])

                if y['n'] not in nums[primes[i + 1]]:
                    nums[primes[i + 1]][y['n']] = []
                nums[primes[i + 1]][y['n']].append(x['n'])


# 0.07 seconds so far :)
#print_r(nums)
#current = nums[primes[0]]
#prime_key = 0
#for key in current:
#    for n in current[key]:
#        for t in current[key][n]
#            temp_set = set(nums[primes[prime_key]])
        #for j in range(1, len(primes) - 1):
        #    current[key] = pand_merge(key, nums[primes[j]][key])

print_r(nums)

print time.time() - start_time, "seconds"
