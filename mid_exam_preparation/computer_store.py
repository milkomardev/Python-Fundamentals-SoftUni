no_tax_total = 0
tax = 0

command = input()

while command != 'special' and command != 'regular':
    price = float(command)
    if price < 0:
        print('Invalid price!')
        command = input()
        continue
    no_tax_total += price
    tax += price * 0.2
    command = input()

total_with_tax = no_tax_total + tax

if command == 'special':
    total_with_tax = total_with_tax * 0.9

if total_with_tax == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {no_tax_total:.2f}$')
    print(f'Taxes: {tax:.2f}$')
    print('-----------')
    print(f'Total price: {total_with_tax:.2f}$')
