import time

start_time = time.time()

cipher = map(int, open('59.txt').read().split(','))


def xor(coded_cipher, key):
    """
    xor the coded cipher with a repeating key
    """
    decoded = []
    for i in xrange(len(coded_cipher)):
        decoded.append(coded_cipher[i] ^ key[i % len(key)])
    return decoded

c, k = [65, 42, 107, 107], [42, 107, 65]


def dictionary_test(string, words):
    """
    Test how many words exist in the given string
    """
    positives = 0
    for w in words:
        if w in string:
            positives += 1
    return positives


def crack():
    """
    Crack the code
    """
    testWords = ['the', 'be', 'to', 'of', 'and']
    global cipher, keyPoss
    for a in keyPoss:
        for b in keyPoss:
            for c in keyPoss:
                key = [ord(a), ord(b), ord(c)]
                dec = xor(cipher, key)
                cracked = ''.join([chr(d) for d in dec])
                if dictionary_test(cracked, testWords) >= 5:
                    print(str(sum(dec)) + " - " + cracked)



keyPoss = [chr(i) for i in range(97, 123)]
crack()

print time.time() - start_time, "seconds"
