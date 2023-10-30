import sys

snowballs = int(input())

max_weight = -sys.maxsize
max_time = -sys.maxsize
max_quality = -sys.maxsize
max_value = -sys.maxsize

for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight/time) ** quality
    if value > max_value:
        max_value = value
        max_time = time
        max_quality = quality
        max_weight = weight

print(f'{max_weight} : {max_time} = {int(max_value)} ({max_quality})')