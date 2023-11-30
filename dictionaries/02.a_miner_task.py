line = input()
resources = {}

while line != 'stop':
    quantity = int(input())
    if line not in resources:
        resources[line] = quantity
    else:
        resources[line] += quantity

    line = input()

for key, value in resources.items():
    print(f"{key} -> {value}")