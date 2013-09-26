def front_times(str, n):
    if len(str) <= 2:
        return str * n
    return str[0:3] * n

print front_times('Abcde', 3)
