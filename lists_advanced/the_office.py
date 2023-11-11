empl_happines = [int(x) for x in input().split()]
factor = int(input())
empl_happines = [factor*x for x in empl_happines]

filtered = [x for x in empl_happines if x >= sum(empl_happines) / len(empl_happines)]

if len(filtered) >= len(empl_happines) / 2:
    print(f'Score: {len(filtered)}/{len(empl_happines)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(empl_happines)}. Employees are not happy!')
    