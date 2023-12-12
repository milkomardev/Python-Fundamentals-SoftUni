path = input().split("\\")
file = path[-1].split('.')
extension = file[-1]
file_name = '.'.join(file[:-1])

print(f"File name: {file_name}")
print(f'File extension: {extension}')

