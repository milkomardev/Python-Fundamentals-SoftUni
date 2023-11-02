numbers = input().split()
message = input()

final_message = ''
msg_as_list = list(message)
for num in numbers:
    total = 0
    for d in num:
        digit = int(d)
        total += digit
    while len(msg_as_list) <= total:
        total = total - len(msg_as_list)

    if len(msg_as_list) > total:
        letter = msg_as_list[total]
        final_message += letter
        msg_as_list.pop(total)

print(final_message)

