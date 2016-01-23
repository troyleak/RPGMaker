#!/usr/bin/env python3
import argparse
from character_gen import *

description_text = 'Create a Pathfinder RPG character'

parser = argparse.ArgumentParser(description=description_text)

parser.add_argument('-m', '--mode', metavar='MODE',
                    choices=[
                        'c', 'r', 'u', 'd',
                        'C', 'R', 'U', 'D',
                        'create', 'read', 'update', 'delete'],
                    help='Mode for this tool - Create/read/update/delete')

parser.add_argument('-l', '--level', action='store', type=int, required=True,
                    choices=range(1, 21),
                    help='Character Level')

parser.add_argument('-s', '--scores', action='append_const', type=int,
                    const=int, required=True, nargs=6,
                    choices=range(1, 19),
                    help='Ability scores in Str Dex Con Int Wis Cha order')

parser.add_argument('-r', '--race', action='store', type=str, required=True,
                    choices=[
                        'dwarf', 'elf', 'gnome', 'half_elf',
                        'half_orc', 'halfling', 'human'
                    ],
                    help='Character\'s Race')

parser.add_argument('-c', '--class', action='store', type=str, required=True,
                    choices=[
                        'barbarian', 'bard', 'cleric', 'druid',
                        'fighter', 'monk', 'paladin', 'ranger',
                        'rogue', 'sorcerer', 'wizard'
                    ],
                    help='Character\'s Class')
