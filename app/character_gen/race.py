'''
Race

Each race's class extends class Race with their attributes

update_stats modifies the parent character with the appropriate stats
    for the race.

'''


# stats argument is a dict containing the ability name and the amount to
# add to the existing stat. Negative numbers will subtract
# like so:
# stats_list =   {"strength":0,
#                 "dexterity":0,
#                 "constitution":0,
#                 "intelligence":0,
#                 "wisdom":0,
#                 "charisma":0 }

# TODO: Fix this vvv


def update_stats(self, master, stats):
    # str, dex, con, int, wis, cha
    # Modifies the parent object with new stats based on the race
    for i, j in stats:
        master.i.stat += j
        master.i.mod += (int(j/2.0))  # For every two points, add a modifier
    print(master.race.race)

# Caps:             # lowercase:
#                   #
# Dwarf             # dwarf
# Elf               # elf
# Gnome             # gnome
# Half_elf          # half_elf
# Half_orc          # half_orc
# Halfling          # halfling
# Human             # human


class Race():
    # generic base class for racial attributes
    def __init__(self):
        self.options = [
            'dwarf', 'halfling', 'elf', 'human',
            'gnome', 'half-orc', 'half-elf']
        self.race = 'none'
        self.traits = {}
        self.languages = []
        self.stats_list = {"": 0}
        self.example_names = {'male': [], 'female': []}

    def make(self, parent, race):
        if race in self.options:
            print("Valid race. Modifying character for racial characteristics")
            if race == 'dwarf':
                parent.race = Dwarf()
                print("dwarf")
            if race == 'halfling':
                parent.race = Halfling()
                print("halfling")
            if race == 'elf':
                parent.race = Elf()
                print("elf")
            if race == 'human':
                parent.race = Human()
                print("human")
            if race == 'gnome':
                parent.race = Gnome()
                print("gnome")
            if race == 'half-orc':
                parent.race = HalfOrc()
                print("half-orc")
            if race == 'half-elf':
                parent.race = HalfElf()
                print("half-elf")
        else:
            print("that race is not an option")


class Dwarf(Race):
    def __init__(self):
        # TODO: Traits description (Possibly defined in feats)
        self.traits = {
            "Slow and Steady": "",
            "Darkvision": "",
            "Defensive Training": "",
            "Greed": "",
            "Hatred": "",
            "Hardy": "",
            "Stability": "",
            "Stonecunning": "",
            "Weapon Familiarity": ""}

        self.languages = ["Common", "Dwarven"]

        self.stats_list = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 2,
            "intelligence": 0,
            "wisdom": 2,
            "charisma": (-2)}

        self.example_names = {
            'male': [
                "Dolgrin",
                "Grunyar",
                "Harsk",
                "Kazmuk",
                "Morgrym",
                "Rogar"],
            'female': [
                "Agna",
                "Bodill",
                "Ingra",
                "Kotri",
                "Rusilka",
                "Yangrit"]}

    def make_dwarf(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        # The attributes object contains a dict options with a member alignment
        # of which we want the second member, chaotic_neutral
        # scale is (0-8), chaotic_evil -> lawful_good
        master.attributes.alignment = alignment.options.alignment[8]


class Elf(Race):
    def __init__(self):
        self.traits = {
            # TODO: Finish example text for racial feats
            "Normal Speed": "Example text goes here",
            "Low-Light Vision": "Example text goes here",
            "Elven Immunities": "Example text goes here",
            "Elven Magic": "Example text goes here",
            "Keen Senses": "Example text goes here",
            "Weapon Familiarity": "Example text goes here"}

        self.languages = ["Common", "Elvish"]

        self.stats_list = {
            "strength": 2,
            "dexterity": 2,
            "constitution": (-2),
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0}

        self.example_names = {
            'male': [
                "Caladrel",
                "Heldadel",
                "Lanliss",
                "Meirdrarel",
                "Seldlon",
                "Talathel",
                "Variel",
                "Zordlon"],
            'female': [
                "Amrunelara",
                "Dardlara",
                "Faunra",
                "Jathal",
                "Merisiel",
                "Oparal",
                "Soumral",
                "Tessara",
                "Yalandlara"]}

    def make_elf(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        master.attributes.alignment = alignment.options.alignment[7]


class Gnome(Race):
    def __init__(self):
        self.traits = {
            "Slow Speed": "",
            "Low-Light Vision": "",
            "Defensive Training": "",
            "Gnome Magic": "",
            "Hatred": "",
            "Illusion Resistance": "",
            "Keen Senses": "",
            "Obsessive": "",
            "Weapon Familiarity": ""}

        self.languages = ["Common", "Gnome", "Sylvan"]

        self.stats_list = {
            "strength": (-2),
            "dexterity": 2,
            "constitution": 2,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 2}

        self.example_names = {
            'male': [
                "Abroshtor",
                "Bastargre",
                "Halungalom",
                "Krolmnite",
                "Poshment",
                "Zarzuket",
                "Zatqualmie"],
            'female': [
                "Besh",
                "Fijit",
                "Lini",
                "Neji",
                "Majet",
                "Pai",
                "Queck",
                "Trig"]}

    def make_gnome(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Small'
        master.languages = self.languages
        master.attributes.alignment = alignment.options.alignment[7]


class HalfElf(Race):
    def __init__(self):
        self.traits = {
            "Normal Speed": "",
            "Low-Light Vision": "",
            "Adaptability": "",
            "Elf Blood": "",
            "Elven Immunities": "",
            "Keen Senses": "",
            "Multitalented": ""}

        self.languages = ["Common", "Elvish"]

# TODO: Implement +2 bonus of user choice at character creation
        self.stats_list = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 2}
# Calathes, Encinal, Kyras, Narciso, Quiray, Satinder, Seltyiel, Zirul
# Cathran, Elsbeth, Iandoli, Kieyanna, Lialda, Maddela, Reda, Tamarie
        self.example_names = {
            'male': [
                "Calathes",
                "Encinal",
                "Kyras",
                "Narciso",
                "Quiray",
                "Satinder",
                "Seltyiel",
                "Zirul"],
            'female': [
                "Cathran",
                "Elsbeth",
                "Iandoli",
                "Kieyanna",
                "Lialda",
                "Maddela",
                "Reda",
                "Tamarie"]}

    def make_half_elf(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        master.attributes.alignment = alignment.options.alignment[2]


class HalfOrc(Race):
    def __init__(self):
        self.traits = {
            "Normal Speed": "",
            "Low-Light Vision": "",
            "Elven Immunities": "",
            "Elven Magic": "",
            "Keen Senses": "",
            "Weapon Familiarity": ""}

        self.languages = ["Common", "Elvish"]
# TODO: Implement choosing +2 at character creation
        self.stats_list = {
            "strength": 2,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0}

        self.example_names = {
            'male': [
                "Caladrel",
                "Heldadel",
                "Lanliss",
                "Meirdrarel",
                "Seldlon",
                "Talathel",
                "Variel",
                "Zordlon"],
            'female': [
                "Amrunelara",
                "Dardlara",
                "Faunra",
                "Jathal",
                "Merisiel",
                "Oparal",
                "Soumral",
                "Tessara",
                "Yalandlara"]}

    def make_half_orc(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        master.attributes.alignment = alignment.options.alignment[1]


class Halfling(Race):
    def __init__(self):
        self.traits = {
            "Slow Speed": "",
            "Fearless": "",
            "Halfling Luck": "",
            "Sure Footed": "",
            "Keen Senses": "",
            "Weapon Familiarity": ""}

        self.languages = ["Common", "Halfling"]

        self.stats_list = {
            "strength": (-2),
            "dexterity": 2,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 2}

        self.example_names = {
            'male': [
                "Antal",
                "Boram",
                "Evan",
                "Jamir",
                "Kaleb",
                "Lem",
                "Miro",
                "Sumak"],
            'female': [
                "Anafa",
                "Bellis",
                "Etune",
                "Filiu",
                "Lissa",
                "Marra",
                "Rillka",
                "Sistra",
                "Yamyra"]}

    def make_halfling(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Small'
        master.languages = self.languages
        master.attributes.alignment = alignment.options.alignment[4]


class Human(Race):
    def __init__(self):
        self.traits = {
            "Normal Speed": "",
            "Bonus Feat": "",
            "Skilled": ""}

        self.languages = ["Common"]
# TODO: Implement choosing +2 at character creation
        self.stats_list = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 2,
            "wisdom": 0,
            "charisma": 0}

        self.example_names = {
            'male': [
                "Caladrel",
                "Heldadel",
                "Lanliss",
                "Meirdrarel",
                "Seldlon",
                "Talathel",
                "Variel",
                "Zordlon"],
            'female': [
                "Amrunelara",
                "Dardlara",
                "Faunra",
                "Jathal",
                "Merisiel",
                "Oparal",
                "Soumral",
                "Tessara",
                "Yalandlara"]}

    def make_human(self, master):
        self.update_stats(master, self.stats_list)
        master.size = 'Medium'
        master.languages = self.languages
        master.attributes.alignment = alignment.options.alignment[2]
    # humans gain one more skill rank per level
