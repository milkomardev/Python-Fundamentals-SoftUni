lines = int(input())
total_sum = 0

for n in range(lines):
    symbol = input()
    total_sum += ord(symbol)

print(f'The sum equals: {total_sum}')

