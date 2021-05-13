import global_variables
from scripts.engine.active_state import *
from scripts.engine.current_active_state import *


def get_available_options():
    available_options = {}
    if CurrentActiveState.ACTIVE_STATE == ActiveStates.WORLD_MAP:
        for key, value in global_variables.game_map.tiles[global_variables.game_map.selected_tile[0]][global_variables.game_map.selected_tile[1]].landscape.get_funcs().items():
            available_options[key] = value
        available_options['Go to local map'] = go_to_local_map
        return available_options
    elif CurrentActiveState.ACTIVE_STATE == ActiveStates.LOCATION_MAP:
        available_options['Go to world map'] = go_to_world_map
        return available_options


def go_to_local_map():
    CurrentActiveState.ACTIVE_STATE = ActiveStates.LOCATION_MAP


def go_to_world_map():
    CurrentActiveState.ACTIVE_STATE = ActiveStates.WORLD_MAP
