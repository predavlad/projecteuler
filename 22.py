import time

start_time = time.time()


def get_name_val(name):
    name_sum = 0
    for i in range(0, len(name)):
        name_sum += ord(name[i]) - 64

    return name_sum

txt = open('22.txt')
names = txt.read().split(',')
names.sort()

total_sum = 0

for i in range(len(names)):
    index = i + 1
    name_sum = get_name_val(names[i])
    total_sum += name_sum * index


print total_sum

print time.time() - start_time, "seconds"
