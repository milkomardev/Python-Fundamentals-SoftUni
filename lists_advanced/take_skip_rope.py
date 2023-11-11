line = list(input())

non_numbers_list = []
numbers_list = []
take_list = []
delete_list = []

[numbers_list.append(int(char)) for char in line if char.isdigit()]
[non_numbers_list.append(char) for char in line if not char.isdigit()]
[take_list.append(numbers_list[num]) for num in range(len(numbers_list)) if num % 2 == 0]
[delete_list.append(numbers_list[num]) for num in range(len(numbers_list)) if num % 2 != 0]

result = []

while take_list:
    for el in range(len(take_list)):
        chr_to_take = take_list[0]
        if chr_to_take > 0:
            for n in range(1, chr_to_take + 1):
                if non_numbers_list:
                    result.append(non_numbers_list[0])
                    non_numbers_list.pop(0)
        take_list.pop(0)

        for i in range(len(delete_list)):
            chr_to_delete = delete_list[0]
            if chr_to_delete > 0:
                for delete in range(1, chr_to_delete + 1):
                    if non_numbers_list:
                        non_numbers_list.pop(0)
                    else:
                        break
                delete_list.pop(0)
            break
        break

print(''.join(result))