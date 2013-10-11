import time

# 0.003
start_time = time.time()


def is_triangle(word):
    global triangles
    word_sum = sum([ord(letter) - 64 for letter in word])

    if word_sum in triangles:
        return True
    return False


triangles = [i * (i + 1) / 2 for i in range(20) if i != 0]
words = open('42.txt').read().split(',')

counter = 0
for word in words:
    if is_triangle(word):
        counter += 1

print counter

print time.time() - start_time, "seconds"
