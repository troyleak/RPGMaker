import random

'''
Contains data structures pertaining to character's physical attributes

class Attributes()
    contains a dict with the available options for each attribute

set_attrib takes an attribute and a value and sets the attribute appropriately,
    if the desired attribute and option exist.
'''

class Attributes():
    def __init__(self):
        self.options = {'gender':['male', 'female'],
                        'size':['large', 'medium', 'small'],
                        'age':list(xrange(18, 400)),
                        'height':list(xrange(100, 200)),
                        'weight':list(xrange(150, 300)),
                        'hair':['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'white'],
                        'eyes':['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'white'],
                        'alignment':{ 'primary':['chaotic', 'neutral', 'lawful'], 'secondary':['evil', 'neutral', 'good']}
                        }

        self.gender = 'none'
        self.size = 'none'
        self.age = 0
        self.height = 0
        self.weight = 0
        self.hair = 'none'
        self.eyes = 'none'
        self.alignment = 'none'


    def set_attrib(self, attrib, value):
    # takes an attribute and a value and sets the value to the passed val
    # checks its own member variables and if that exists, the list of
    # options for that attribute before modifying the value
    # TODO: Move to try/except

        if attrib in self.__dict__ and value in self.options[attrib]:
            self.__dict__[attrib] = value
        else:
            print("Error modifying that attribute. Perhaps it doesn't exist?")
        print("test")


    def set_attribs_rand(self):
        # sets attributes randomly
        self.gender = random.choice(self.options[gender])
        self.race = random.choice(self.options[race])
        self.size = random.choice(self.options[size])
        self.age = random.choice(self.options[age])
        self.height = random.choice(self.options[height])
        self.weight = random.choice(self.options[weight])
        self.hair = random.choice(self.options[hair])
        self.eyes = random.choice(self.options[eyes])
        self.alignment = random.choice(self.options[alignment])
