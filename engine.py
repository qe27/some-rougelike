import copy
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
from scripts.engine.handlers.main_keyboard_handler import handle_keys
from scripts.engine.handlers.main_mouse_handler import handle_mouse
from scripts.engine.handlers.messages_handle import get_action_messages
from scripts.game_states import GameStates
from scripts.input_handlers import get_pressed_key
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
    # test copy (works!)
    ship2 = copy.deepcopy(global_variables.player.ship)
    ship2.set_tile(global_variables.game_map.tiles[10][10])
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

        key_action = get_pressed_key(key, CurrentActiveState.ACTIVE_STATE)
        if mouse.lbutton_pressed:
            handle_mouse(mouse)
        if key_action:
            handle_keys(key_action, wm_next_hour_executor)

        clear_all(global_variables.CONSOLE, CurrentActiveState.ACTIVE_STATE)


if __name__ == '__main__':
    main()