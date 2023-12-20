# import re
# pattern = r'\d+'
# numbers = []
# while True:
#     text = input()
#     if not text:
#         break
#
#     matches = re.findall(pattern, text)
#     numbers.extend(matches)
# print(' '.join(numbers))

text = input().lower().replace(' ', '_')

print(text)