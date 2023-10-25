budget = int(input())

command = input()
amount_left = budget

while command != "End":
    price = int(command)
    amount_left -= price
    if amount_left < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print(f'You bought everything needed.')
