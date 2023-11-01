items = input().split('|')
budget = float(input())

new_price_list = []
profits = 0
for item in items:
    item_args = item.split('->')
    item_type = item_args[0]
    price = float(item_args[1])

    if item_type == 'Clothes' and price > 50.00:
        continue
    if item_type == 'Shoes' and price > 35.00:
        continue
    if item_type == 'Accessories' and price > 20.50:
        continue
    if budget < price:
        continue

    budget -= price
    new_price_list.append(price*1.4)
    profits += (price*1.4 - price)

total_money = budget + sum(new_price_list)

for new in new_price_list:
    print(f'{new:.2f}', end=' ')

print('')
print(f'Profit: {profits:.2f}')

if total_money >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
