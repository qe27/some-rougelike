from scripts.engine.active_state import *
from scripts.engine.current_active_state import *

CONSOLE = None
map_offset = (0, 0)
selected_tile = (0, 0)
selected_ship_layer = 0
selected_object = None
tile_info_options = {}
object_options = {}
map_width = 100
map_height = 60
game_map = None
player = None


def get_current_map():
    if CurrentActiveState.ACTIVE_STATE == ActiveStates.WORLD_MAP:
        return game_map
    if CurrentActiveState.ACTIVE_STATE == ActiveStates.LOCATION_MAP:
        return game_map.get_local_map()
    if CurrentActiveState.ACTIVE_STATE == ActiveStates.SHIP_MAP:
        return player.ship.model.get(selected_ship_layer)
