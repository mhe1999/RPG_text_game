from classes.game import  person, bcolors
from classes.magic import spell
from classes.Inventory import Item

#some black magic
fire = spell('Fire', 10, 100, 'black')
thunder = spell('Thunder', 10, 100, 'black')
blizzard = spell('Blizzard', 10, 100, 'black')
meteor= spell('Meteor', 20, 200, 'black')
quake = spell('Quake', 14, 140, 'black')

#some white magic
cure = spell('Cure', 12, 120, 'white')
cura = spell('Cura', 18, 200, 'white')

#create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

#Instantiate people
player = person(460, 65, 60, 34,
                [fire, thunder, blizzard, meteor, cure, cura],
                [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}])
enemy = person(1200, 65, 45, 25, [], [])

Running = True

#print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACK' + bcolors.ENDC)


while Running:
    print('=====================')
    player.choose_action()
    choice = int(input(('Choose action:'))) - 1
    #print('you choose' , player.get_spell_name(int(choice) - 1))

    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + 'you attacked for ' + str(dmg) + ' pints of damage' + bcolors.ENDC)

    elif choice == 1:
        player.choose_magic()
        magic_choice = int(input('choose magic:')) - 1
        if magic_choice == -1:
            continue
        # magic_dmg = player.generate_spell_damage(magic_choice)
        # spell_name = player.get_spell_name(magic_choice)
        # spell_cost = player.get_spell_cost(magic_choice)

        magic_dmg = player.magic[magic_choice].generate_damage()

        if player.magic[magic_choice].get_cost() > player.get_mp():
            print(bcolors.FAIL + '\nnot enough MP\n' , bcolors.ENDC)
            continue

        player.reduce_mp(player.magic[magic_choice].get_cost())

        if player.magic[magic_choice].get_type() == 'black' :
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + '\n' + player.magic[magic_choice].get_name() + ' deals ' + str(magic_dmg) + ' points of damage ' + bcolors.ENDC)
        elif player.magic[magic_choice].get_type() == 'white' :
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + '\n' + player.magic[magic_choice].get_name() + ' heals you by ' + str(magic_dmg) + ' points ' + bcolors.ENDC)


    if choice == 2:
        player.choose_item()
        item_choice = int(input('choose item:')) - 1
        if item_choice == -1:
            continue

        if player.items[item_choice]['quantity'] == 0:
            print(bcolors.FAIL + 'there is no ' +  player.items[item_choice]['item'].get_name() + ' left' + bcolors.ENDC)
            continue

        else:
            player.items[item_choice]['quantity'] -= 1

        if player.items[item_choice]['item'].get_type() == 'potion':
            player.heal(player.items[item_choice]['item'].get_prop())
            print(bcolors.OKGREEN + '\n' + player.items[item_choice]['item'].get_name() +
                  ' heals for ' + str(player.items[item_choice]['item'].get_prop()) + 'HP' + bcolors.ENDC)

        elif player.items[item_choice]['item'].get_type() == 'elixer':
            player.heal(player.items[item_choice]['item'].get_prop())
            print(bcolors.OKGREEN + '\n' + player.items[item_choice]['item'].get_name() +
                  ' restore your HP ' + bcolors.ENDC)

        elif player.items[item_choice].get_type() == 'attack':
            enemy.take_damage(player.items[item_choice]['item'].get_prop())
            print(bcolors.FAIL + '\n' + player.items[item_choice]['item'].get_name() +
                  ' deeals ' +  str(player.items[item_choice]['item'].get_prop()) + 'point of damage' +bcolors.ENDC)


    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(bcolors.FAIL+'enemy attack for '+ str(enemy_damage) + bcolors.ENDC)

    print('--------------------')
    print('enemy hp:' + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print('player hp:' + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print('player mp:' + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC+'\n')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN +'you win!' , bcolors.ENDC)
        Running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL +'you have lost!' , bcolors.ENDC)
        Running = False
