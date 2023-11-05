import math


def line_length(a1, b1, a2, b2):
    return ((abs(a1) + abs(a2)) * (abs(b1) + abs(b2))) / 2


def distance_from_center(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        return f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})'
    elif abs(x2 + y2) <= abs(x1 + y1):
        return f'({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})'


a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

ab_length = line_length(a1, b1, a2, b2)
xy_length = line_length(x1, y1, x2, y2)

if ab_length >= xy_length:
    print(distance_from_center(a1, b1, a2, b2))
else:
    print(distance_from_center(x1, y1, x2, y2))