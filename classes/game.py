import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ['Attack' , 'Magic' , 'items']

    def generate_damage(self):
        return random.randrange(self.atkl , self.atkh)


    def take_damage(self , dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp >= self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        print('\n' + self.name + ':')
        print(bcolors.OKBLUE + bcolors.BOLD +'    Actions:' + bcolors.ENDC)
        for i in range(len(self.actions)):
            print('       ' ,i+1 , ':' , self.actions[i])


    def choose_magic(self):
        print('\n' + bcolors.OKBLUE + bcolors.BOLD +'    Magics:' + bcolors.ENDC)
        for i in range(len(self.magic)):
            print('       ' ,i+1 , ':' , self.magic[i].get_name() , '(cost :' , self.magic[i].get_cost(), ')')


    def choose_item(self):
        print('\n' + bcolors.OKGREEN + bcolors.BOLD +'    Items:' + bcolors.ENDC)
        for i in range(len(self.items)):
            print('       ' ,i+1 , ':' , self.items[i]['item'].get_name() , ' : ' , self.items[i]['item'].get_descrption(), self.items[i]['quantity'])



    def choose_target(self, enemies):
        i = 1

        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        print('\n\n\n')
        return choice

    def get_stat(self):
        hpbar_len = int(self.hp / self.maxhp * 25)
        mpbar_len = int(self.mp / self.maxmp * 10)
        hpbar = mpbar = ''

        for i in range(25):
            if i <= hpbar_len:
                hpbar += '█'
            else:
                hpbar += '▒'

        for i in range(10):
            if i <= mpbar_len:
                mpbar += '█'
            else:
                mpbar += '▒'

        print('_________________________'.rjust(48)  +  '__________'.rjust(25))
        print(bcolors.BOLD + (self.name +':').ljust(10) + (str(self.hp) + '/' + str(self.maxhp)).rjust(12) + '|' + bcolors.OKGREEN +
            hpbar+ bcolors.ENDC + '|' + (str(self.mp) + '/' + str(self.maxmp)).rjust(13) + '|'
            +bcolors.BOLD+bcolors.OKBLUE+mpbar+bcolors.ENDC+'|')


    def get_enemy_stat(self):
        hpbar_len = int(self.hp / self.maxhp * 50)
        hpbar = ''
        for i in range(50):
            if i<=hpbar_len:
                hpbar += '█'
            else:
                hpbar += '▒'

        print(('_'*50).rjust(73))
        print(bcolors.BOLD + (self.name + ':').ljust(10) + (str(self.hp) + '/' + str(self.maxhp)).rjust(12) + '|' + bcolors.FAIL + hpbar + bcolors.ENDC + bcolors.BOLD + '|' + bcolors.ENDC)
