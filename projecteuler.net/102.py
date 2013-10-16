import time
# 0.008 seconds
start_time = time.time()


def get_area(a, b, c):
    return abs(a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - b[0]*a[1] - c[0]*b[1] - a[0]*c[1]) / 2


def get_center(a, b, c):
    return (a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1] / 3.0)


def is_inside(a, b, c):
    """
    Check if O = (0, 0) is inside the triangle formed by the points a, b, c

    I first calculate the area of the main triangle. Afterwards, I calculate the sum of the areas
    of the 3 triangles that can be formed with the origin and 2 other points. If the point is inside,
    they should be equal
    """
    main_area = get_area(a, b, c)
    O = (0, 0)
    areas = sum([get_area(a, b, O), get_area(b, c, O), get_area(c, a, O)])
    return areas <= main_area


points = [i.split(",") for i in open('102.txt').read().split("\n") if i != ""]
counter = 0

for pairs in points:
    pairs = map(int, pairs)
    A, B, C = pairs[0:2], pairs[2:4], pairs[4:6]
    if is_inside(A, B, C):
        counter += 1

print counter

print time.time() - start_time, "seconds"
