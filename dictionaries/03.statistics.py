line = input()
products_in_stock = {}
while line != 'statistics':
    key, value = line.split(': ')
    value = int(value)
    if key not in products_in_stock:
        products_in_stock[key] = value
    else:
        products_in_stock[key] += value

    line = input()

print('Products in stock:')

for key, value in products_in_stock.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products_in_stock)}")
print(f"Total Quantity: {sum(products_in_stock.values())}")

