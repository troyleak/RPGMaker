def update_stats( self, master, stats ): # str, dex, con, int, wis, cha
    # Stats is a dict containing the abilty name and the amount to modify
    # like so:
    # stats_list =   {"strength":0,
    #                 "dexterity":0,
    #                 "constitution":0,
    #                 "intelligence":0,
    #                 "wisdom":0,
    #                 "charisma":0 }
    # the modifier is adjusted based on this
    for i, j in stats:
        master.i.stat += j
        master.i.mod += (int(j/2.0)) # For every two points, add a modifier

    print("Ability Stats updated")

    # def random():
    #     options = {'race':['dwarf', 'halfling', 'elf', 'human', 'gnome', 'half-orc', 'half-elf']}
    #
    #     self.race = 'none'


class Dwarf():
    def __init__(self, master):
        # TODO: Traits description (Possibly defined in feats)
        self.traits =  {"Slow and Steady":"",
                        "Darkvision":"",
                        "Defensive Training":"",
                        "Greed":"",
                        "Hatred":"",
                        "Hardy":"",
                        "Stability":"",
                        "Stonecunning":"",
                        "Weapon Familiarity":"" }

        self.languages = ["Common","Dwarven"]

        self.stats_list =   {"strength":0,
                        "dexterity":0,
                        "constitution":2,
                        "intelligence":0,
                        "wisdom":2,
                        "charisma":(-2) }

        if (master.gender == 'male'):
            self.example_names = ["Dolgrin", "Grunyar", "Harsk", "Kazmuk", "Morgrym", "Rogar"]
            print("male names initialized")
        if (master.gender == 'female'):
            self.example_names = ["Agna", "Bodill", "Ingra", "Kotri", "Rusilka", "Yangrit"]
            print("female names initialized")



    def make(self, master):
        # Updates namedtuple for stat and modifier
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        print("test")
    # dostuff


class Elf():
    def __init__(self, master):
        self.traits = []

    def make():
        print("test")
    # dostuff


class Gnome():
    def __init__(self, master):
        self.traits = []

    def make():
        print("test")
    # dostuff


class Half_elf():
    def __init__(self, master):
        self.traits = []

    def make():
        print("test")
    # dostuff


class Half_orc():
    def __init__(self, master):
        self.traits = []

    def make():
        print("test")
    # dostuff


class Halfling():
    def __init__(self, master):
        self.traits = []

    def make():
        print("test")
    # dostuff


class Human():
    def __init__(self, master):
        self.traits = []

    def make():
        print("test")
    # dostuff
    # humans gain one more skill rank per level

class Race():
    def __init__(self):
        print("test")
