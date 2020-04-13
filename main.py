from classes.game import  person, bcolors
magic = [{'name' : 'Fire', 'cost' : 10 , 'dmg' : 100},
        {'name' : 'Thunder', 'cost' : 10 , 'dmg' : 124},
        {'name' : 'Blizzard', 'cost' : 10 , 'dmg' : 100}]

player = person(460, 65, 60, 34, magic)
enemy = person(1200, 65, 45, 25, magic)

Running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACK' + bcolors.ENDC)


while Running:
    print('=====================')
    player.choose_action()
    choice = int(input(('Choose action:'))) - 1
    #print('you choose' , player.get_spell_name(int(choice) - 1))

    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('you attacked for' , dmg , 'pints of damage')

    elif choice == 1:
        player.choose_magic()
        magic_choice = int(input('choose magic:')) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell_name = player.get_spell_name(magic_choice)
        spell_cost = player.get_spell_cost(magic_choice)

        if spell_cost > player.get_mp():
            print(bcolors.FAIL + '\nnot enough MP\n' , bcolors.ENDC)
            continue

        player.reduce_mp(spell_cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + '\n' + spell_name + ' deals ' + str(magic_dmg) + ' points of damage ' + bcolors.ENDC)

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print('enemy attack for' , enemy_damage)

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
