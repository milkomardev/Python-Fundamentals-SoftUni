lines = int(input())

opening_counter = 0
closing_counter = 0

balanced = True

for i in range(lines):
    action = input()
    if action != "(" and action != ")":
        continue
    if action == '(':
        opening_counter += 1
        if opening_counter > closing_counter + 1:
            balanced = False
    if action == ')':
        closing_counter += 1
        if closing_counter > opening_counter:
            balanced = False

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
