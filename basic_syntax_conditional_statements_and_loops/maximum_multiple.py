import sys

divisor = int(input())
boundary = int(input())

max_number = -sys.maxsize

for b in range(1, boundary + 1):
    if b % divisor == 0:
        max_number = b

print(max_number)


# for b in range(boundary, 0, -1):
#     if b % divisor == 0:
#         print(b)
#         break
