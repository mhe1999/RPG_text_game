from classes.game import  person, bcolors
from classes.magic import spell
from classes.Inventory import Item
import  random
import copy


#some black magic
fire = spell('Fire', 10, 600, 'black')
thunder = spell('Thunder', 10, 600, 'black')
blizzard = spell('Blizzard', 10, 600, 'black')
meteor= spell('Meteor', 20, 1200, 'black')
quake = spell('Quake', 14, 140, 'black')

#some white magic
cure = spell('Cure', 12, 620, 'white')
cura = spell('Cura', 18, 1500, 'white')

#create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 10}, {"item": hipotion, "quantity": 1},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 3},
                {"item": hielixer, "quantity": 1}, {"item": grenade, "quantity": 3}]


#Instantiate people
player1 = person('valos', 10000, 95, 300, 34, player_spells, copy.deepcopy(player_items))
player2 = person('nick', 4168, 50, 311, 34, player_spells, copy.deepcopy(player_items))
player3 = person('robot', 3089, 80, 288, 34, player_spells, copy.deepcopy(player_items))
enemy1 = person('IMP', 1600, 130, 560, 325, player_spells, [])
enemy2 = person('magus', 10000, 221, 525, 25,player_spells, [])
enemy3 = person('IMP', 1100, 130, 560, 325,player_spells, [])

Running = True

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

while Running:
    for player in players:

        print('\n')
        print('NAME                   HP                                      MP')
        for i in players:
            i.get_stat()
        for enemy in enemies:
            enemy.get_enemy_stat()

        player.choose_action()
        choice = int(input(('Choose action:'))) - 1

        #player choose to attack
        if choice == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            print(bcolors.OKBLUE + 'you attacked '+bcolors.ENDC + bcolors.FAIL +
                enemies[enemy].name + bcolors.ENDC + bcolors.OKBLUE + ' for ' +
                 str(dmg) + ' pints of damage' + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + ' has died')
                del enemies[enemy]

        #player choose to use magic
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input('choose magic:')) - 1

            if magic_choice == -1: #go to last page
                continue

            magic_dmg = player.magic[magic_choice].generate_damage()

            if player.magic[magic_choice].get_cost() > player.get_mp():
                print(bcolors.FAIL + '\nnot enough MP\n' , bcolors.ENDC)
                continue

            player.reduce_mp(player.magic[magic_choice].get_cost())

            #use black magic(which damage the enemy)
            if player.magic[magic_choice].get_type() == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + '\n' + player.magic[magic_choice].get_name() +
                    ' deals ' + str(magic_dmg) + ' points of damage to ' +
                    bcolors.ENDC + bcolors.FAIL+ enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + 'has died')
                    del enemies[enemy]

            #use white magic(which heal the player)
            elif player.magic[magic_choice].get_type() == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + player.magic[magic_choice].get_name() +
                    ' heals you by ' + str(magic_dmg) + ' points ' + bcolors.ENDC)

        #player choose to use Items
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

            #use one of the potions which heal the player
            if player.items[item_choice]['item'].get_type() == 'potion':
                player.heal(player.items[item_choice]['item'].get_prop())
                print(bcolors.OKGREEN + '\n' + player.items[item_choice]['item'].get_name() +
                      ' heals for ' + str(player.items[item_choice]['item'].get_prop()) + 'HP' + bcolors.ENDC)

            #use elixer which restore HP/MP completly
            elif player.items[item_choice]['item'].get_type() == 'elixer':
                if player.items[item_choice]['item'].get_name() == 'Elixer':
                    player.heal(player.items[item_choice]['item'].get_prop())
                    print(bcolors.OKGREEN + '\n' + player.items[item_choice]['item'].get_name() +
                          ' restore your HP ' + bcolors.ENDC)
                else:
                    for i in players:
                        i.heal(i.items[item_choice]['item'].get_prop())
                    print(bcolors.OKGREEN + '\n' + i.items[item_choice]['item'].get_name() +
                          ' restore all parties HP ' + bcolors.ENDC)

                player.heal(player.items[item_choice]['item'].get_prop())
                print(bcolors.OKGREEN + '\n' + player.items[item_choice]['item'].get_name() +
                      ' restore your HP ' + bcolors.ENDC)


            #use attack items which damage the enemy
            elif player.items[item_choice]['item'].get_type() == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(player.items[item_choice]['item'].get_prop())
                print(bcolors.OKBLUE + '\n' + player.items[item_choice]['item'].get_name() +
                      ' deeals ' +  str(player.items[item_choice]['item'].get_prop()) +
                      'point of damage to '+ bcolors.ENDC +bcolors.FAIL + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + 'has died')
                    del enemies[enemy]

    #determine winner when all player or enemies dead
    if len(enemies) == 0:
        print(bcolors.OKGREEN +'you won!' , bcolors.ENDC)
        Running = False
        continue

    #enemies attacking or use magics
    for enemy in enemies:
        enemy_choice = random.randrange(0,2)
        target = random.randrange(0,len(players))
        if enemy_choice == 0:
            enemy_damage = enemy.generate_damage()
            players[target].take_damage(enemy_damage)
            print(bcolors.FAIL+ enemy.name + ' attack ' + players[target].name + ' for '+ str(enemy_damage) + bcolors.ENDC)


        elif enemy_choice == 1:
            affordable_magic = list()
            for i in enemy.magic:
                if i.get_cost() < enemy.get_mp():
                    affordable_magic.append(i)

            if len(affordable_magic) > 0:
                magic_choice = random.randrange(0 , len(affordable_magic))
                dmg = affordable_magic[magic_choice].generate_damage()
                enemy.reduce_mp(affordable_magic[magic_choice].get_cost())
                if affordable_magic[magic_choice].get_type() == 'black':
                    players[target].take_damage(dmg)
                    print(enemy.name + ' use ' + affordable_magic[magic_choice].get_name() +
                        ' to damage ' + players[target].name + ' for ' + str(dmg))

                elif affordable_magic[magic_choice].get_type() == 'white':
                    enemy.heal(dmg)
                    print(enemy.name + ' use ' + affordable_magic[magic_choice].get_name() +
                        ' to heal himself for ' + str(dmg))

            else:
                print('there is no magic that ' + enemy.name + ' can use')
        if players[target].get_hp() == 0:
            print(players[target].name + ' has died')
            del players[target]

    if len(players) == 0:
        print(bcolors.FAIL +'you have lost!' , bcolors.ENDC)
        Running = False
