text = input()

[print(f"{text[idx]}{text[idx + 1]}") for idx in range(len(text)) if text[idx] == ':']
# for idx in range(len(text)):
#     if text[idx] == ':':
#         print(f"{text[idx]}{text[idx + 1]}")