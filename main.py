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
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]
#Instantiate people
player1 = person('valos', 10000, 132, 300, 34, player_spells, copy.deepcopy(player_items))
player2 = person('nick', 4168, 188, 311, 34, player_spells, copy.deepcopy(player_items))
player3 = person('robot', 3089, 174, 288, 34, player_spells, copy.deepcopy(player_items))
enemy1 = person('IMP', 1250, 130, 560, 325, [], [])
enemy2 = person('magus', 18200, 221, 525, 25, [], [])
enemy3 = person('IMP', 1250, 130, 560, 325, [], [])

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
        if choice == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print(bcolors.OKBLUE + 'you attacked '+bcolors.ENDC + bcolors.FAIL + enemies[enemy].name + bcolors.ENDC + bcolors.OKBLUE + ' for ' + str(dmg) + ' pints of damage' + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + 'has died')
                del enemies[enemy]
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input('choose magic:')) - 1
            if magic_choice == -1:
                continue

            magic_dmg = player.magic[magic_choice].generate_damage()

            if player.magic[magic_choice].get_cost() > player.get_mp():
                print(bcolors.FAIL + '\nnot enough MP\n' , bcolors.ENDC)
                continue

            player.reduce_mp(player.magic[magic_choice].get_cost())

            if player.magic[magic_choice].get_type() == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + '\n' + player.magic[magic_choice].get_name() +
                    ' deals ' + str(magic_dmg) + ' points of damage to ' + bcolors.ENDC + bcolors.FAIL+ enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + 'has died')
                    del enemies[enemy]
            elif player.magic[magic_choice].get_type() == 'white':
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

            elif player.items[item_choice]['item'].get_type() == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(player.items[item_choice]['item'].get_prop())
                print(bcolors.OKBLUE + '\n' + player.items[item_choice]['item'].get_name() +
                      ' deeals ' +  str(player.items[item_choice]['item'].get_prop()) + 'point of damage to '+ bcolors.ENDC +bcolors.FAIL + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + 'has died')
                    del enemies[enemy]
    enemy_choice =random.randrange(0,3)
    enemy_damage = enemies[0].generate_damage()
    players[enemy_choice].take_damage(enemy_damage)
    print(bcolors.FAIL+'enemy attack ' + players[enemy_choice].name + ' for '+ str(enemy_damage) + bcolors.ENDC)

    #print('--------------------')

    defeated_enemies = 0
    for i in enemies:
        if i.get_hp() == 0:
            defeated_enemies += 1
    if defeated_enemies == len(enemies):
        print(bcolors.OKGREEN +'you win!' , bcolors.ENDC)
        Running = False

    defeated_players = 0
    for i in players:
        if i.get_hp() == 0:
            defeated_players += 1
    if defeated_players == len(players):
        print(bcolors.FAIL +'you have lost!' , bcolors.ENDC)
        Running = False
