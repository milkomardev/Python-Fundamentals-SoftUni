from string import ascii_letters,digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + '-' + '_'

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    chars_as_list = [char in allowed_chars for char in username]
    valid_chars_only = all(chars_as_list)

    if valid_chars_only:
        print(username)



