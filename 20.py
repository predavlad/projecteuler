import time

start_time = time.time()

product = 1
for i in range(2, 101):
    product *= i

product = str(product)
fact_sum = 0
for i in range(0, len(product)):
    fact_sum += int(product[i])

print fact_sum

print time.time() - start_time, "seconds"
