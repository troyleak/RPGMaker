def update_stats( self, master, stats ): # str, dex, con, int, wis, cha
    # Modifies the parent object with new stats based on the race
    for i, j in stats:
        master.i.stat += j
        master.i.mod += (int(j/2.0)) # For every two points, add a modifier
    # stats argument is a dict containing the ability name and the amount to
    # add to the existing stat. Negative numbers will subtract
    # like so:
    # stats_list =   {"strength":0,
    #                 "dexterity":0,
    #                 "constitution":0,
    #                 "intelligence":0,
    #                 "wisdom":0,
    #                 "charisma":0 }

# Dwarf
# Elf
# Gnome
# Half_elf
# Half_orc
# Halfling
# Human
#
# dwarf
# elf
# gnome
# half_elf
# half_orc
# halfling
# human


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

        self.stats_list =  {"strength":0,
                            "dexterity":0,
                            "constitution":2,
                            "intelligence":0,
                            "wisdom":2,
                            "charisma":(-2) }

        self.example_names =   {'male':["Dolgrin", "Grunyar", "Harsk", "Kazmuk", "Morgrym", "Rogar"],
                             'female':["Agna", "Bodill", "Ingra", "Kotri", "Rusilka", "Yangrit"] }



    def make_dwarf(self, master):
        # Updates namedtuple for stat and modifier
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        print("test")
    # dostuff


class Elf():
    def __init__(self, master):
        self.traits =  {"Normal Speed":"",
                        "Low-Light Vision":"",
                        "Elven Immunities":"",
                        "Elven Magic":"",
                        "Keen Senses":"",
                        "Weapon Familiarity":"" }

        self.languages = ["Common","Elvish"]

        self.stats_list =  {"strength":2,
                            "dexterity":2,
                            "constitution":(-2),
                            "intelligence":0,
                            "wisdom":0,
                            "charisma":0 }

        self.example_names =   {'male':["Caladrel", "Heldadel", "Lanliss", "Meirdrarel", "Seldlon", "Talathel", "Variel", "Zordlon"],
                             'female':["Amrunelara", "Dardlara", "Faunra", "Jathal", "Merisiel", "Oparal", "Soumral", "Tessara", "Yalandlara"] }

    def make_elf():
        print("test")
    # dostuff


class Gnome():
    def __init__(self, master):
        self.traits = []

    def make_gnome():
        print("test")
    # dostuff


class Half_elf():
    def __init__(self, master):
        self.traits = []

    def make_half_elf():
        print("test")
    # dostuff


class Half_orc():
    def __init__(self, master):
        self.traits = []

    def make_half_orc():
        print("test")
    # dostuff


class Halfling():
    def __init__(self, master):
        self.traits = []

    def make_halfling():
        print("test")
    # dostuff


class Human():
    def __init__(self, master):
        self.traits = []

    def make_human():
        print("test")
    # dostuff
    # humans gain one more skill rank per level

class Race():
    def __init__(self):
        self.options = ['dwarf', 'halfling', 'elf', 'human', 'gnome', 'half-orc', 'half-elf']
        self.race = 'none'
        self.traits =  {'':''}
        self.languages = []
        self.stats_list =  {"":0}
        self.example_names =   {'male':[], 'female':[] }
