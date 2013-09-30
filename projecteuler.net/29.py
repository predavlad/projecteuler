import time

start_time = time.time()

def generate_squares(start, end):
    squares = []
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            squares.append(i ** j)

    squares = list(set(squares))
    return squares

squares = generate_squares(2, 100)
print squares
print len(squares)

print time.time() - start_time, "seconds"
