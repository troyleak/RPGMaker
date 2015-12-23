RPGMaker
=========

Simple Pathfinder character sheet and NPC generator.

Allows the user to specify certain stats, and fills in the remaining stats with
random values. At the end, allows the user to modify any value to their liking

Once created, the character sheet can be submitted.


To begin, clone the Repo

navigate to the directory

[code]
conda env create

source activate RPGMaker

python3 project/RPGMaker
[/code]

Documentation for RPGMaker project

Character Generation:

Order:
1. Ability Scores
2. Race
3. Class
4. Skills/Feats
5. Gear
6. Attributes

Character:
Base class for items related to character creation. Each aspect of the character will be represented in this class. This object will be passed around and modified by the different classes.



Dice:
Contains functions for dice rolls and modifiers. Most of the math will be done here


Ability Scores:
SetScores: Takes 6 values. If none are recieved (or they're all zero), generates random values for the character by calling dice rollxdy(x, y) and applies them, then calls SetMods to fill in modifiers.

SetMods: Sets ability score modifiers based on existing stats. Called at the end of SetScores.



Attributes:
LOW PRIORITY - Right now just takes text from user and adds it to the charsheet. Eventually want to have selection from list based on race, class, etc. Will be done after other scores have been input.



Class:
Contains logic for setting the character's class.

Each of the seven classes contains a function "make" which takes the character object as an argument, and the desired level.



Feats:
TODO - Contains a list of feats and their descriptions. Contains functions to add to misc modifiers for permanent feats, and add a text description to situational feats




Gear:
AddItem(): add an item of gear to the character's backpack.
RemoveItem(): remove an item of gear from the character's backpack.
ListItems(): returns an iterable containing a list of the items in the character's backpack




Race:
Contains logic for creating a specific race character. Will be run once on creation, modifying this stat will require a regeneration of the character's base class, destroying user-defined mods and such. If you want to select a different race, I recommend backing up any stats you're attached to, as they will be wiped and/or randomly regenerated. Contains a "make" function which takes the character as an argument and modifies it to include race-specific traits. So calling dwarf.make() will do something different than half_orc.make(), but both can be included with a wildcard or by directly importing the needed one.



Skills:
Contains logic for adding to, subtracting from, modifying, and displaying the skill list. Contains a variable with the number of unspent skill points.

add_skill_points(): Function to calculate skill points. Run at level up time. Takes the character's class and intelligence and adds the appropriate amount to the skill points stat. Call this function in a loop to level up multiple times.

spend_skill_points(): Function to subtract skill points. Takes the skill, and number of levels. Automatically deducts the correct number of skill points from the character.


TODO - Spells:
