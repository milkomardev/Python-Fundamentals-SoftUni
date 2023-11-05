def loading_bar(number):
    percent = ''
    dot = ''
    if number % 10 == 0:
        percent = (number // 10) * "%"
        dot = (10 - number // 10) * '.'
    return f'[{percent}{dot}]'


input_number = int(input())

if input_number == 100:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
else:
    print(f'{input_number}% {loading_bar(input_number)}')
    print('Still loading...')
