#!/usr/bin/env python3
import argparse
from character_gen import *

description_text = 'Create a Pathfinder RPG character'

parser = argparse.ArgumentParser(description=description_text)

parser.add_argument('-m', '--mode', metavar='$MODE',
                    choices=[
                        'c', 'r', 'u', 'd',
                        'C', 'R', 'U', 'D',
                        'create', 'read', 'update', 'delete'],
                    help='Mode for this tool - Create/read/update/delete')

parser.add_argument('-s', '--scores', type=int, required=True, nargs=6,
                    choices=range(1, 19),
                    metavar='$SCORE',
                    help='Ability scores in Str Dex Con Int Wis Cha order\
                        between 1 and 18')

parser.add_argument('-r', '--race', type=str, required=True, metavar='$RACE',
                    choices=[
                        'dwarf', 'elf', 'gnome', 'half_elf',
                        'half_orc', 'halfling', 'human'
                    ],
                    help='Character\'s Race')

parser.add_argument('-c', '--class', type=str, required=True, metavar='$CLASS',
                    dest='char_class',
                    choices=[
                        'barbarian', 'bard', 'cleric', 'druid',
                        'fighter', 'monk', 'paladin', 'ranger',
                        'rogue', 'sorcerer', 'wizard'
                    ],
                    help='Character\'s Class')

args = parser.parse_args()
print(args)

if args.mode in ['c', 'C', 'create']:
    # create our character
    char = character.Character()

    # assign stats
    stat_labels = char.abilities.stats.keys()
    ability_scores = dict(zip(stat_labels, args.scores))
    char.abilities.set_ability_scores(ability_scores)

    # assign race
    char.race.make(char, args.race)

    # assign class
    char.char_class.make(args.char_class)

    print(char.to_json())

elif args.mode in ['r', 'R', 'read']:
    print(char.to_json())  # not pretty but works for now

elif args.mode in ['u', 'U', 'update']:
    print("Not supported (yet)")

elif args.mode in ['d', 'D', 'delete']:
    print("Not supported (yet)")
