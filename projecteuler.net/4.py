def check_palindrome(nr):
    return str(nr) == str(nr)[::-1]


def find_palindromes(length):
    min = int('1' + '0' * (length - 1))
    max = int('9' * length) + 1
    print min, max
    maxPal = 0
    for i in reversed(range(min, max)):
        for j in reversed(range(min, max)):
            nr = i * j
            if check_palindrome(nr):
                if nr > maxPal:
                    maxPal = nr
    return maxPal


print find_palindromes(3)
