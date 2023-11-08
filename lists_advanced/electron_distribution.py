electrons = int(input())
shells = []

while electrons > 0:
    n = len(shells)+1
    max_electrons_in_shell = 2*n**2
    shells.append(min(max_electrons_in_shell, electrons))
    electrons -= max_electrons_in_shell

print(shells)