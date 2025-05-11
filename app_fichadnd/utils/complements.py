from random import randint

TRANSLATIONS = {
    'charname_label':        {'pt': 'Nome do Personagem',               'en': 'Character Name'},
    'classlevel_label':      {'pt': 'Classe e Nível',                   'en': 'Class & Level'},
    'background_label':      {'pt': 'Antecedente',                      'en': 'Background'},
    'playername_label':      {'pt': 'Nome do Jogador',                  'en': 'Player Name'},
    'race_label':            {'pt': 'Raça',                             'en': 'Race'},
    'alignment_label':       {'pt': 'Alinhamento',                      'en': 'Alignment'},
    'experiencepoints_label':{'pt': 'Pontos de Experiência',            'en': 'Experience Points'},

    'strength_label':        {'pt': 'Força',                            'en': 'Strength'},
    'dexterity_label':       {'pt': 'Destreza',                         'en': 'Dexterity'},
    'constitution_label':    {'pt': 'Constituição',                     'en': 'Constitution'},
    'wisdom_label':          {'pt': 'Sabedoria',                        'en': 'Wisdom'},
    'intelligence_label':    {'pt': 'Inteligência',                     'en': 'Intelligence'},
    'charisma_label':        {'pt': 'Carisma',                          'en': 'Charisma'},

    'inspiration_label':     {'pt': 'Inspiração',                       'en': 'Inspiration'},
    'proficiencybonus_label':{'pt': 'Bônus de Proficiência',            'en': 'Proficiency Bonus'},
    'savingthrows_label':    {'pt': 'Testes de Resistência',            'en': 'Saving Throws'},
    'skills_label':          {'pt': 'Perícias',                         'en': 'Skills'},
    'passiveperception_label':{'pt': 'Percepção Passiva (Percepção)',   'en': 'Passive Wisdom (Perception)'},
    'otherprofs_label':      {'pt': 'Outras Proficiências e Idiomas',   'en': 'Other Proficiencies and Languages'},

    'armorclass_label':      {'pt': 'Classe de Armadura',              'en': 'Armor Class'},
    'initiative_label':      {'pt': 'Iniciativa',                       'en': 'Initiative'},
    'speed_label':           {'pt': 'Movimento',                        'en': 'Speed'},
    'maxhp_label':           {'pt': 'Pontos de Vida Máximos',           'en': 'Hit Point Maximum'},
    'currenthp_label':       {'pt': 'Pontos de Vida Atuais',            'en': 'Current Hit Points'},
    'temphp_label':          {'pt': 'Pontos de Vida Temporários',       'en': 'Temporary Hit Points'},

    'totalhd_label':         {'pt': 'Total',                            'en': 'Total'},
    'remaininghd_label':     {'pt': 'Dados de Vida',                    'en': 'Hit Dice'},
    'death_saves_label':     {'pt': 'Testes de Morte',                  'en': 'Death Saves'},
    'successes_label':       {'pt': 'Sucessos',                         'en': 'Successes'},
    'failures_label':        {'pt': 'Falhas',                           'en': 'Failures'},

    'attacks_spellcasting_label': {'pt': 'Ataques e Magias',            'en': 'Attacks & Spellcasting'},
    'atkname_label':         {'pt': 'Nome',                             'en': 'Name'},
    'atkbonus_label':        {'pt': 'Bônus de Ataque',                  'en': 'Atk Bonus'},
    'atkdamage_label':       {'pt': 'Dano/Tipo',                        'en': 'Damage/Type'},

    'equipment_label':       {'pt': 'Equipamento',                     'en': 'Equipment'},
    'cp_label':              {'pt': 'cp',                               'en': 'cp'},
    'sp_label':              {'pt': 'sp',                               'en': 'sp'},
    'ep_label':              {'pt': 'ep',                               'en': 'ep'},
    'gp_label':              {'pt': 'gp',                               'en': 'gp'},
    'pp_label':              {'pt': 'pp',                               'en': 'pp'},

    'personality_label':     {'pt': 'Personalidade',                    'en': 'Personality'},
    'ideals_label':          {'pt': 'Ideais',                           'en': 'Ideals'},
    'bonds_label':           {'pt': 'Vínculos',                         'en': 'Bonds'},
    'flaws_label':           {'pt': 'Defeitos',                         'en': 'Flaws'},
    'features_traits_label': {'pt': 'Características e Traços',         'en': 'Features & Traits'},

    'spells': {'pt': 'Magias', 'en': 'Spells'},
    'spellcasting_header': {'pt': 'Conjuração', 'en': 'Spellcasting'},
    'spellcasting_ability': {'pt': 'Habilidade de Conjuração', 'en': 'Spellcasting Ability'},
    'spell_save_dc': {'pt': 'CD para Resistencia', 'en': 'Spell Save DC'},
    'spell_attack_bonus': {'pt': 'Bônus de Ataque de Magia', 'en': 'Spell Attack Bonus'},
    'proficiency': {'pt': 'Bônus de Proficiência', 'en': 'Proficiency Bonus'},

    'spell_slots': {'pt': 'Espaços de Magia', 'en': 'Spell Slots'},
    'level': {'pt': 'Nível', 'en': 'Level'},
    'used': {'pt': 'Usados', 'en': 'Used'},
    'total': {'pt': 'Total', 'en': 'Total'},

    'spell_cantrips': {'pt': 'Truques', 'en': 'Cantrips'},
    'spell_level': {'pt': 'Nível', 'en': 'Level'},
}

LANGUAGES = [
    "Abyssal", "Celestial", "Common", "Draconic", "Deep Speech",
    "Infernal", "Primordial", "Sylvan", "Undercommon", "Elvish", "Dwarvish",
    "Gnomish", "Halfling", "Orc", "Goblin"
]

MOD_TABLE = {
    1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2,
    7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1,
    13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4,
    19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7,
    25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10
}

proficiency_by_level = [2, 2, 2, 2,   
                        3, 3, 3, 3,  
                        4, 4, 4, 4,   
                        5, 5, 5, 5,  
                        6, 6, 6, 6]   

MOD_TABLE = {
    1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2,
    7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1,
    13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4,
    19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7,
    25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10
}

XP_BY_LEVEL = {
    1:   0,
    2:   300,
    3:   900,
    4:   2700,
    5:   6500,
    6:   14000,
    7:   23000,
    8:   34000,
    9:   48000,
    10:  64000,
    11:  85000,
    12: 100000,
    13: 120000,
    14: 140000,
    15: 165000,
    16: 195000,
    17: 225000,
    18: 265000,
    19: 305000,
    20: 355000
}


RESIST_MAP = {
    ("ST Strength",      "STR"),
    ("ST Dexterity",     "DEX"),
    ("ST Constitution",  "CON"),
    ("ST Intelligence",  "INT"),
    ("ST Wisdom",        "WIS"),
    ("ST Charisma",      "CHA"),
}

SKILLS_MAP = {
    "Acrobatics":    "DEX",
    "Arcana":        "INT",
    "Athletics":     "STR",
    "Performance":   "CHA",
    "Persuasion":    "CHA",
    "Stealth":       "DEX",
    "Deception":     "CHA",
    "History":       "INT",
    "Investigation": "INT",
    "Perception":    "WIS",
    "Medicine":      "WIS",
    "Nature":        "INT",
    "Insight":       "WIS",
    "Intimidation":  "CHA",
    "SleightofHand": "DEX",
    "Survival":      "WIS",
    "Animal":        "WIS",
    "Religion":      "INT"
}

API_TO_PDF_SKILL = {
    "skill-acrobatics":      "Acrobatics",
    "skill-animal-handling": "Animal",
    "skill-arcana":          "Arcana",
    "skill-athletics":       "Athletics",
    "skill-deception":       "Deception ",
    "skill-history":         "History ",
    "skill-insight":         "Insight",
    "skill-intimidation":    "Intimidation",
    "skill-investigation":   "Investigation ",
    "skill-medicine":        "Medicine",
    "skill-nature":          "Nature",
    "skill-perception":      "Perception ",
    "skill-performance":     "Performance",
    "skill-persuasion":      "Persuasion",
    "skill-sleight-of-hand": "SleightofHand",
    "skill-stealth":         "Stealth ",
    "skill-survival":        "Survival",
    "skill-religion":        "Religion",
}

pool = [
    {"name":"Shortsword","die":6,"type":"melee"},
    {"name":"Longsword","die":8,"type":"melee"},
    {"name":"Dagger","die":4,"type":"melee"},
    {"name":"Quarterstaff","die":6,"type":"melee"},
    {"name":"Light Crossbow","die":8,"type":"ranged"},
    {"name":"Handaxe","die":6,"type":"melee"},
    {"name":"Spear","die":6,"type":"melee"},
]

def gen_atributos():
    atributo = sum(sorted([randint(1, 6) for _ in range(4)])[1:])

    return atributo

