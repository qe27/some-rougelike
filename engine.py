import tcod as libtcod

import global_variables
from global_variables import *
from map_objects.game_map import WorldMap
from map_objects.map_manager import MapManager
from rendering.render_functions import render_all, clear_all
from rendering.screen_options import *
from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
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
    game_state = GameStates.PAUSED
    debug = True
    CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG

    bar_width = 20
    message_x = bar_width + 2
    message_width = SCREEN_WIDTH - bar_width - 2
    message_height = M_PANEL_HEIGHT - 1

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'white': libtcod.Color(250, 250, 250),
        'yellow': libtcod.Color(250, 250, 0)
    }

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'shop game', False)

    global_variables.CONSOLE = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    MapManager.map = WorldMap(map_width, map_height)
    # MapManager.map.make_map()

    additional_render_params = {}

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    # selected_tile = (0, 0)

    message_log = MessageLog(message_x, message_width, message_height)
    action_panel_messages = []

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        render_all(colors, game_state, action_panel_messages, game_map=MapManager.map)
        libtcod.console_flush()

        action_panel_messages = get_action_messages()
        key_action = handle_keys(key, game_state)
        selector_move = key_action.get('selector_move')
        # selector_move = key_action.get('key_1')
        action = key_action.get('action')

        if mouse.lbutton_pressed:
            handle_mouse(mouse)

        if selector_move:
            global_variables.selected_tile = tuple(map(operator.add, global_variables.selected_tile, selector_move))

        clear_all(global_variables.CONSOLE, MapManager.map)

        if debug:
            handle_debug(MapManager.map.tiles[global_variables.selected_tile[0]][global_variables.selected_tile[1]], action_panel_messages, key_action)


if __name__ == '__main__':
    main()