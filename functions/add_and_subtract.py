def add(a,b):
    return first + second


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

sum_result = add(first, second)
sum_subtract = subtract(sum_result, third)

print(sum_subtract)