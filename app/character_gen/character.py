
'''
Default constructor creates empty values.
Call set_attribs_rand method on Character object to populate with random
values
Call set_attrib to change an individual parameter
'''
import json
from . import ability_scores, attributes, classes, feats, gear, race, skills, spells

class Character(): # TODO: Add feats

    def __init__(self):
        self.valid_form_field_values = [
            'abilities','weapon','race','char_class','skills','gear',
            'attributes','feats','spells','money','experience', 'armor']


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
        if stat in self.__dict__:
            self.stat = scores
        else:
            print("Error assigning stat " + stat)
        # TODO: Finish this

    def assign_stats_from_submitted_list(self, form_list):
        json_char = self.char_to_json()
        for entry in form_list:
            for i in self.valid_form_field_values:
                if entry[1] == (None or 0 or ''):
                    print("No value input for " + entry[0])
                    break
                elif i in entry[0]:
                    print( "Writing " + str(entry[1]) + " to character in " + str(entry[0])) # j represents the
                    break


    def char_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4) # from https://stackoverflow.com/questions/3768895/python-how-to-make-a-class-json-serializable
