line = input()
products = {}
while line != 'buy':
    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

    line = input()

for key, value in products.items():
    print(f"{key} -> {products[key][0] * products[key][1]:.2f}")