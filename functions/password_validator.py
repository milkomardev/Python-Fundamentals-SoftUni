def is_valid_length(password):
    return 6 <= len(password) <= 10


def consist_only_letters_and_digits(password):
    return password.isalnum()


def has_two_digits(password):
    digit_counter = 0
    for ch in password:
        if ch.isdigit():
            digit_counter += 1
    return digit_counter >= 2


input_password = input()
is_valid = True

if not is_valid_length(input_password):
    print('Password must be between 6 and 10 characters')
    is_valid = False

if not consist_only_letters_and_digits(input_password):
    print('Password must consist only of letters and digits')
    is_valid = False

if not has_two_digits(input_password):
    print('Password must have at least 2 digits')
    is_valid = False

if is_valid:
    print('Password is valid')
