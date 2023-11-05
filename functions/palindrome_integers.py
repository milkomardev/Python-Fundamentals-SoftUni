def is_palindrome(numbers):
    for nums in numbers:
        digits = list(nums)
        if digits == list(reversed(digits)):
            print('True')
        else:
            print("False")


numbers_as_str = input().split(', ')

is_palindrome(numbers_as_str)
