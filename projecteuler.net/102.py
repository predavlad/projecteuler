import time
# 0.008 seconds
start_time = time.time()


def get_area(a, b, c):
    """
    Calculate the area of the zone formed by the 3 points a, b and c
    """
    return abs(a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - b[0]*a[1] - c[0]*b[1] - a[0]*c[1]) / 2


def is_inside(a, b, c, p):
    """
    Check if p = (0, 0) is inside the triangle formed by the points a, b, c

    I first calculate the area of the main triangle. Afterwards, I calculate the sum of the areas
    of the 3 triangles that can be formed with the origin and 2 other points. If the point is inside,
    they should be equal
    """
    return get_area(a, b, c) >= sum([get_area(a, b, p), get_area(b, c, p), get_area(c, a, p)])


points = [i.split(",") for i in open("102.txt").read().split("\n") if i != ""]
counter = 0

for pairs in points:
    pairs = map(int, pairs)
    if is_inside(pairs[0:2], pairs[2:4], pairs[4:6], (0, 0)):
        counter += 1

print counter

print time.time() - start_time, "seconds"
