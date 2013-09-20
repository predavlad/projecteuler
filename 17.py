# to be done

import time
#import num2word
import math

start_time = time.time()

print num2word.to_cart(342)

digits = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

tens = {
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
    90: 'ninety'
}

multiples = {
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million'
}


#def transform_nr(nr):
#	temp = nr
#	text_nr = ''
#	while temp > 1:
#		if temp % 1000000:
#			text_nr += digits[math.floor(temp / 1000000)]




print time.time() - start_time, "seconds"

