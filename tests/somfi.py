from itertools import permutations
import csv

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
              'r', 's', 't', 'v', 'w', 'x', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']


csv_vowels_2 = []
csv_vowels_3 = []
csv_consonants_2 = []
csv_consonants_3 = []

for i in permutations(vowels, 2):
    csv_vowels_2.append(''.join(i))

for i in permutations(vowels, 3):
    csv_vowels_3.append(''.join(i))

for i in permutations(consonants, 2):
    csv_consonants_2.append(''.join(i))

for i in permutations(consonants, 3):
    csv_consonants_3.append(''.join(i))

vowels_csv = open('vowels.csv', 'wb')
wr = csv.writer(vowels_csv, quoting=csv.QUOTE_NONE)
for i in range(len(csv_vowels_3)):
    if i >= len(csv_vowels_2):
        wr.writerow([csv_vowels_3[i]])
    else:
        wr.writerow([csv_vowels_3[i], csv_vowels_2[i]])

consonants_csv = open('consonants.csv', 'wb')
wr = csv.writer(consonants_csv, quoting=csv.QUOTE_NONE)
for i in range(len(csv_consonants_3)):
    if i >= len(csv_consonants_2):
        wr.writerow([csv_consonants_3[i]])
    else:
        wr.writerow([csv_consonants_3[i], csv_consonants_2[i]])


print csv_vowels_2
print csv_vowels_3
print csv_consonants_2
print csv_consonants_3



