import time
import itertools
from itertools import izip, cycle

start_time = time.time()


def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(data, cycle(key)))


def decryptXOR(s, key="\x101Z"):
    output = ""
    for character in s:
        for letter in key[::-1]:
            character = chr(ord(character) ^ ord(letter))
        output += character
    return output


def descipher(txt, key):
    desciphered_text = ''
    current_key = 0
    key_len = 3
    for i in txt:
        new_ascii = int(key[current_key] ^ int(i))
        desciphered_text += chr(new_ascii)
        current_key += 1
        current_key %= key_len

    return desciphered_text


# key = [ord('('), ord('T'), ord('h')]
# print key

txt = open('59.txt').read().split(',')
key = [40, 84, 104]
txt = map(chr, map(int, txt))
print txt
# print map(chr, range(97, 123))
# keys = range(97, 123)
# shown = 0
#
# print 40 ^ 79, 84 ^ 59, 104 ^ 12

print decryptXOR(txt, key)

# for i in list(itertools.combinations(keys, 3)):
#     desciphered_text = descipher(txt, i)
#     if desciphered_text:
#         shown += 1
#         print desciphered_text
#
# print shown

# print descipher(txt)

print time.time() - start_time, "seconds"
