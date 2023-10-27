key = int(input())
lines = int(input())

message = ''
for n in range(lines):
    symbol = input()
    dec_symbol = ord(symbol) + key
    message += chr(dec_symbol)

print(message)