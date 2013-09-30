# identical code as #18
import time

start_time = time.time()

txt = open('67.txt')
triangle = txt.read()


def split_text(text):
    return text.split(' ')


matrix = map(split_text, triangle.split("\n"))

for i in range(len(matrix) - 1, -1, -1):
    for j in range(i, -1, -1):
        matrix[i][j] = int(matrix[i][j])

for i in range(len(matrix) - 2, -1, -1):
    for j in range(i, -1, -1):
        nr_checked = [matrix[i + 1][j], matrix[i + 1][j + 1]]
        matrix[i][j] += max(nr_checked)

print matrix[0][0]

print time.time() - start_time, "seconds"

