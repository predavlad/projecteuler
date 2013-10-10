import time

start_time = time.time()


def get_name_val(name):
    name_sum = 0
    for i in xrange(0, len(name)):
        name_sum += ord(name[i]) - 64

    return name_sum


names = open('22.txt').read().split(',')
names.sort()
total_sum = 0


for i in xrange(len(names)):
    index = i + 1
    total_sum += get_name_val(names[i]) * index


print total_sum

print time.time() - start_time, "seconds"
