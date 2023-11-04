import math


def distance_from_center(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        return f'({math.floor(x1)}, {math.floor(y1)})'
    elif abs(x2 + y2) <= abs(x1 + y1):
        return f'({math.floor(x2)}, {math.floor(y2)})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance_from_center(x1, y1, x2, y2))
