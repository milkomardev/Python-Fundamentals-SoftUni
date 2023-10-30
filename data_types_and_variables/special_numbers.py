n = int(input())

# for num in range(1, n+1):
#     digit_to_string = str(num)
#     digit_sum = 0
#     is_special = False
#     for char in digit_to_string:
#         digit_sum += int(char)
#         if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
#             is_special = True
#
#     print(f'{num} -> {is_special}')

for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = digits // 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
