from enum import Enum


class Races(Enum):
    HUMAN = {
        'stats': {
            'max_health': 80,
            'max_mana': 40,
            'str': 4,
            'dex': 4,
            'int': 4,
            'luck': 4
        },
        'abilities': {}
    }
    MAGIC_ELEMENTAL = {
        'stats': {
            'max_health': 40,
            'max_mana': 80,
            'str': 4,
            'dex': 4,
            'int': 4,
            'luck': 4
        },
        'abilities': {}
    }