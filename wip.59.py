import time


start_time = time.time()
cipher = map(int, open('59.txt').read().split(','))
# key = [40, 84, 104]


def xor(bytes, keyBytes):
    returnValue = []
    # print bytes
    print keyBytes
    for i in range(0, len(bytes)):
        returnValue.append(bytes[i] ^ keyBytes[i % len(keyBytes) - 1])
    return returnValue


def dictionaryTest(string, words):
    positives = 0
    for w in words:
        if w in string:
            positives += 1
    return positives


# def crack():
#     testWords = ['the', 'be', 'to', 'of', 'and']
#     global cipher, keyPoss
#     for a in keyPoss:
#         for b in keyPoss:
#             for c in keyPoss:
#                 key = [ord(a), ord(b), ord(c)]
#                 dec = xor(cipher, key)
#                 cracked = ''.join([chr(d) for d in dec])
#                 if dictionaryTest(cracked, testWords) >= 5:
#                     print(str(sum(dec)) + " - " + cracked)


keyPoss = [chr(i) for i in range(97, 123)]
key = [ord('g'), ord('o'), ord('d')]
print map(chr, xor(cipher, key))

print time.time() - start_time, "seconds"
