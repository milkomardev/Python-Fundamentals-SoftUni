def even_and_odd_sums(number):
    sum_even = 0
    sum_odd = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    return [sum_even, sum_odd]


num_as_str = input()

even_and_odd_sums(num_as_str)
result = even_and_odd_sums(num_as_str)
print(f'Odd sum = {result[1]}, Even sum = {result[0]}')
