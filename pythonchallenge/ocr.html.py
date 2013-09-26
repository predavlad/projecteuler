import time

start_time = time.time()

txt = open('chars.txt').read().replace("\n", '')
letters = {}
for letter in txt:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1

print letters

print time.time() - start_time, "seconds"

# equality