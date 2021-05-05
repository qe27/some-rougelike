WORLD_MAP = 'WORLD'
LOCATION_MAP = 'LOCATION'
BATTLE_MAP = 'BATTLE'
SHIP_MAP = 'SHIP'


def get_next_map_type(type):
    if type == WORLD_MAP:
        return LOCATION_MAP
    if type == LOCATION_MAP:
        raise ValueError('No submaps for location map')
