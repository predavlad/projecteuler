import time

start_time = time.time()

# should run or about 5 seconds
def find_numbers():
	for i in range(1, 999):
	    for j in range(i, 999):
	        for k in range(j, 999):
	            if (i + j + k) == 1000:
	                if i * i + j * j == k * k:
	                    return i, j, k

print find_numbers()

print time.time() - start_time, "seconds"
