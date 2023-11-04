def data_types(type_of_data, number):
    if type_of_data == 'int':
        number = int(number)
        result = number * 2
    elif type_of_data == 'real':
        number = float(number)
        result = f'{number*1.5:.2f}'
    else:
        result = f'${number}$'
    return result


type_of_data = input()
command = input()

print(data_types(type_of_data,command))
