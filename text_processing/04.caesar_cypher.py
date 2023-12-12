line = list(input())
line = [chr(ord(line[idx]) + 3) for idx in range(len(line))]
print(''.join(line))

# for idx in range(len(line)):
#     line[idx] = chr(ord(line[idx]) + 3)
# print(''.join(line))