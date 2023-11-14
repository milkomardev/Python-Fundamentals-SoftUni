days = int(input())
plunder_per_day = int(input())
target = float(input())

total_plunder = 0
for day in range(1, days + 1):
    total_plunder += plunder_per_day

    if day % 3 == 0:
        total_plunder += plunder_per_day*0.5
    if day % 5 == 0:
        total_plunder = total_plunder * 0.7

if total_plunder >= target:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {((total_plunder / target) * 100):.2f}% of the plunder.')
