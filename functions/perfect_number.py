def is_perfect(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number


input_number = int(input())

if is_perfect(input_number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
