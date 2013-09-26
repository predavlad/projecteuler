def near_hundred(n):
    return 90 <= n <= 110 or 190 <= n <= 210

assert near_hundred(93) == True
assert near_hundred(90) == True
assert near_hundred(89) == False