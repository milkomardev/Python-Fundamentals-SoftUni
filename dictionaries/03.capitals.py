countries = input().split(', ')
capitals = input().split(', ')
my_dict = {}

for idx in range(len(countries)):
    my_dict[countries[idx]] = capitals[idx]

for key, value in my_dict.items():
    print(f"{key} -> {value}")