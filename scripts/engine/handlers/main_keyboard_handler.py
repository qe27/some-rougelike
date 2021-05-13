import operator

import global_variables
from global_variables import get_current_map
from rendering.screen_options import MAIN_PANEL_WIDTH, MAIN_PANEL_HEIGHT


def handle_keys(key_action, wm_next_hour_executor):
    selector_move = key_action.get('selector_move')
    offset_move = key_action.get('offset_move')
    # selector_move = key_action.get('key_1')
    toggle_pause = key_action.get('toggle_pause')
    action = key_action.get('action')

    if toggle_pause:
        if wm_next_hour_executor.is_running:
            wm_next_hour_executor.stop()
        else:
            wm_next_hour_executor.start()

    current_map = get_current_map()

    if offset_move:
        current_map.map_offset = tuple(map(operator.add, current_map.map_offset, offset_move))
        if current_map.map_offset[0] < 0:
            current_map.map_offset = (0, current_map.map_offset[1])
        if current_map.map_offset[1] < 0:
            current_map.map_offset = (current_map.map_offset[0], 0)
        if current_map.map_offset[0] > current_map.width - MAIN_PANEL_WIDTH:
            current_map.map_offset = (max(current_map.width - MAIN_PANEL_WIDTH, 0), current_map.map_offset[1])
        if current_map.map_offset[1] > current_map.height - MAIN_PANEL_HEIGHT:
            current_map.map_offset = (current_map.map_offset[0], max(current_map.height - MAIN_PANEL_HEIGHT, 0))

    if selector_move:
        current_map.selected_tile = tuple(map(operator.add, current_map.selected_tile, selector_move))
        if current_map.selected_tile[0] < 0:
            current_map.selected_tile = (0, current_map.selected_tile[1])
        if current_map.selected_tile[1] < 0:
            current_map.selected_tile = (current_map.selected_tile[0], 0)
        if current_map.selected_tile[0] >= current_map.width:
            current_map.selected_tile = (current_map.width - 1, current_map.selected_tile[1])
        if current_map.selected_tile[1] >= current_map.height:
            current_map.selected_tile = (current_map.selected_tile[0], current_map.height - 1)

    if key_action.get('key_0'):
        global_variables.selected_ship_layer = 0
    if key_action.get('key_1'):
        global_variables.selected_ship_layer = 1