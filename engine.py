from datetime import datetime
import tcod as libtcod

import global_variables
from global_variables import *
from map_objects.game_map import Map
from objects.game_objects.player import Player

from objects.game_objects.prepared_objects import ships
from rendering.render_functions import render_all, clear_all
from rendering.screen_options import *
from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
from scripts.engine.end_turn_manager import world_map_next_hour
from scripts.engine.executor import Executor
from scripts.engine.game_messages import MessageLog
from scripts.engine.handlers.debug_handler import handle_debug
from scripts.engine.handlers.key_handlers.selected_options import SelectedOptions
from scripts.engine.handlers.main_mouse_handler import handle_mouse
from scripts.engine.handlers.messages_handle import get_action_messages
from scripts.game_states import GameStates
from scripts.input_handlers import handle_keys
import operator


def main():
    global map_width
    global map_height
    debug = True
    CurrentActiveState.ACTIVE_STATE = ActiveStates.WORLD_MAP

    bar_width = 20
    message_x = bar_width + 2
    message_width = SCREEN_WIDTH - bar_width - 2
    message_height = M_PANEL_HEIGHT - 1

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'shop game', False)

    global_variables.CONSOLE = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    global_variables.game_map = Map(map_width, map_height)
    global_variables.player = Player()
    global_variables.player.ship = ships[0]
    global_variables.player.ship.set_tile(global_variables.game_map.tiles[0][0])
    # MapManager.map.make_map()

    additional_render_params = {}

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    # selected_tile = (0, 0)
    # print(str(ships_map))

    message_log = MessageLog(message_x, message_width, message_height)
    action_panel_messages = []

    wm_next_hour_executor = Executor(0.3, world_map_next_hour)

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        render_all(CurrentActiveState.ACTIVE_STATE, action_panel_messages)
        libtcod.console_flush()

        # action_panel_messages = get_action_messages()
        key_action = handle_keys(key, CurrentActiveState.ACTIVE_STATE)
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

        if mouse.lbutton_pressed:
            handle_mouse(mouse)

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
                current_map.selected_tile = (current_map.selected_tile[0], current_map.height-1)

        if key_action.get('key_0'):
            global_variables.selected_ship_layer = 0
        if key_action.get('key_1'):
            global_variables.selected_ship_layer = 1

        clear_all(global_variables.CONSOLE, CurrentActiveState.ACTIVE_STATE)
        # if int(datetime.now().strftime('%S')) % 2 == 0:
        # world_map_next_hour()

        # if debug:
        #     handle_debug(current_map.tiles[current_map.selected_tile[0]][current_map.selected_tile[1]], action_panel_messages, key_action)


if __name__ == '__main__':
    main()