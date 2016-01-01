
import json
from . import ability_scores, attributes, classes
from . import feats, gear, race, skills, spells

'''
This is the main class for the model of the character

It contains the submitted values for a character after form submission.

Of note are the functions to assign character values, and to return the
    character object as JSON formatted data

Before form submission, the object contains empty values. The subclasses are
    also configured likewise (for ones in which that is possible).

After form submission, blank values are randomized (within the bounds of
    the other specified values). This means the system is 'lazy' in its
    creating your character.

After the character has been created, it is not possible to go back and alter
    it. I recommend starting from scratch. It may be helpful to outline some
    basic characteristics on paper before using this tool, as it is very much
    in alpha stages and could explode at any moment.

Because of the complexity involved in leveling up a character, the opposite is
    low on my priorities compared to implementing things like feats and spells

'''


class Character():  # TODO: Add feats

    def __init__(self):
        self.valid_form_field_values = [
            'abilities', 'weapon', 'race', 'char_class', 'skills', 'gear',
            'attributes', 'feats', 'spells', 'money', 'experience', 'armor']

        self.abilities = ability_scores.Abilities()
        self.race = race.Race()
        self.char_class = classes.Char_Class()
        self.skills = skills.Skills()
        self.feats = feats.Feats()
        self.spells = spells.Spells()
        self.gear = gear.Gear()
        self.attributes = attributes.Attributes()

        self.money = 0
        self.experience = 0

    def assign_stats(self, stat, scores):
        # because of how the form is submitted, values come
        # in the form of ('class-attrib', 'value')
        if stat in self.__dict__:
            self.stat = scores
        else:
            print("Error assigning stat " + stat)
        # TODO: Finish this - Need to screen stats

    def assign_stats_from_submitted_list(self, form_list):
        for entry in form_list:

            for i in self.valid_form_field_values:

                if entry[1] == (None or 0 or ''):
                    print("No value input for " + entry[0])
                    break

                elif i in entry[0]:
                    print("Writing " + str(entry[1]) + " to " + str(entry[0]))
                    # i needs to be converted from weapons/armor/items to gear
                    # self.assign_stats(i, entry[1])
                    break

    def char_to_json(self):
        return json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# https://stackoverflow.com/questions/3768895/python-how-to-make-a-class-json-serializable
