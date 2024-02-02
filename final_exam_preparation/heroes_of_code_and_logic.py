n = int(input())
heroes = {}
for _ in range(n):
    hero, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[hero] = {'hp': hp, 'mp': mp}

command = input()

while command != 'End':
    command = command.split(' - ')
    action = command[0]
    hero = command[1]
    if action == 'CastSpell':
        needed_mp = int(command[2])
        spell = command[3]
        if needed_mp > heroes[hero]['mp']:
            print(f'{hero} does not have enough MP to cast {spell}!')
        else:
            heroes[hero]['mp'] -= needed_mp
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['mp']} MP!")

    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        heroes[hero]['hp'] -= damage
        if heroes[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif action == 'Recharge':
        amount = int(command[2])
        old_mp = heroes[hero]['mp']
        heroes[hero]['mp'] = min(200, heroes[hero]['mp'] + amount)
        print(f"{hero} recharged for {heroes[hero]['mp'] - old_mp} MP!")

    elif action == 'Heal':
        amount = int(command[2])
        old_hp = heroes[hero]['hp']
        heroes[hero]['hp'] = min(100, heroes[hero]['hp'] + amount)
        print(f"{hero} healed for {heroes[hero]['hp'] - old_hp} HP!")

    command = input()

for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero]['hp']}")
    print(f"  MP: {heroes[hero]['mp']}")