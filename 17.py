import time

start_time = time.time()

num2words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


# naive implementation that only works for max 1000
def transform_nr(n):
    s = ''
    if n == 1000 or n == 100:
        return 'one ' + num2words[n]
    if n > 100:
        digit = n // 100
        s += num2words[digit] + ' ' + num2words[100]
        remainder = n - digit * 100
        if remainder:
            s += ' and ' + transform_nr(remainder)
        return s
    if n > 20:
        digit = n // 10
        s += num2words[digit * 10]
        remainder = n - digit * 10
        if remainder:
            s += '-' + num2words[remainder]
        return s
    return num2words[n]


def get_number_len(n):
    return len(transform_nr(n).replace(' ', '').replace('-', ''))

assert transform_nr(1000) == 'one thousand'
assert transform_nr(100) == 'one hundred'
assert get_number_len(342) == 23
assert get_number_len(115) == 20

letter_counter = [get_number_len(i) for i in range(1, 1001)]
print letter_counter
print sum(letter_counter)

print time.time() - start_time, "seconds"

