import time

start_time = time.time()


def is_triangle(word):
    global triangles
    word_sum = 0
    for letter in word:
        word_sum += ord(letter) - 64

    if word_sum in triangles:
        return True
    return False


triangles = [i * (i + 1) / 2 for i in range(20) if i != 0]
words = open('42.txt').read().split(',')

assert is_triangle("SKY")
assert not is_triangle("SKIA")


counter = 0
for i in range(len(words)):
    if is_triangle(words[i]):
        counter += 1

print counter

print time.time() - start_time, "seconds"
