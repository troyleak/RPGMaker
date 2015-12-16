from flask_wtf import Form
from wtforms import validators, StringField

class Skills:
    def __init__(self, master):
        skills =  { 'acrobatics' : 0,
                    'appraise' : 0,
                    'bluff' : 0,
                    'climb' : 0,
                    'craft_a' : 0,
                    'craft_b' : 0,
                    'craft_c' : 0,
                    'diplomacy' : 0,
                    'disable_device' : 0,
                    'disguise' : 0,
                    'escape_artist' : 0,
                    'fly' : 0,
                    'handle_animal' : 0,
                    'heal' : 0,
                    'intimidate' : 0,
                    'knowledge_arcana' : 0,
                    'knowledge_dungeoneering' : 0,
                    'knowledge_engineering' : 0,
                    'knowledge_geography' : 0,
                    'knowledge_history' : 0,
                    'knowledge_local' : 0,
                    'knowledge_nature' : 0,
                    'knowledge_nobility' : 0,
                    'knowledge_planes' : 0,
                    'knowledge_religion' : 0,
                    'linguistics' : 0,
                    'perception' : 0,
                    'perform_a' : 0,
                    'perform_b' : 0,
                    'profession_a' : 0,
                    'profession_b' : 0,
                    'ride' : 0,
                    'sense_motive' : 0,
                    'sleight_of_hand' : 0,
                    'spellcraft' : 0,
                    'stealth' : 0,
                    'survival' : 0,
                    'swim' : 0,
                    'use_magic_device' : 0 }
