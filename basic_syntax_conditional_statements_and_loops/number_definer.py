number = float(input())

if number == 0:
    print('zero')
elif number < 0:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1_000_000:
        print('large negative')
    elif 1< abs(number) < 1_000_000:
        print('negative')
else:
    if abs(number) < 1:
        print('small positive')
    elif abs(number) > 1_000_000:
        print('large positive')
    elif 1 < abs(number) < 1_000_000:
        print('positive')


