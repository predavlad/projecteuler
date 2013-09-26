import operator
import time

start_time = time.time()

txt = open('chars.equality.txt').read().replace("\n", '')
letters = {}
for letter in txt:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1

print letters
print len(letters)
print min(letters.values())

print sorted(letters.iteritems(), key=operator.itemgetter(1))

print time.time() - start_time, "seconds"

# i K H Z C E I