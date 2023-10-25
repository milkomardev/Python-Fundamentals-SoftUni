number = int(input())

number_in_str = str(number)
list_of_digits = []
for char in number_in_str:
    char_as_int = int(char)
    list_of_digits.append(char_as_int)

list_of_digits.sort(reverse=True)

for i in list_of_digits:
    print(i, end='')
