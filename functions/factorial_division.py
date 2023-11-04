def afact_divided_by_bfact(a, b):
    a_fact = 1
    b_fact = 1
    for nums in range(1, a + 1):
        a_fact = a_fact * nums
    for nums in range(1, b + 1):
        b_fact = b_fact * nums
    return a_fact / b_fact


first = int(input())
second = int(input())

result = afact_divided_by_bfact(first, second)

print(f'{result:.2f}')
