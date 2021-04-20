import time

import tcod as libtcod

from map_objects.game_map import WorldMap
from map_objects.map_manager import MapManager
from render_functions import render_all, clear_all
from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
from scripts.engine.game_messages import MessageLog
from scripts.engine.handlers.debug_handler import handle_debug
from scripts.engine.handlers.key_handlers.debug_key_handler import handle
from scripts.engine.handlers.messages_handle import get_action_messages
from scripts.game_states import GameStates
from scripts.input_handlers import handle_keys
import operator


def main():
    screen_width = 80
    screen_height = 80
    a_panel_height = screen_height // 5
    m_panel_height = screen_height - a_panel_height
    panel_width = screen_width // 3
    map_width = 80
    map_height = 45
    # game_state = GameStates.PAUSED
    game_state = GameStates.PAUSED
    debug = True
    CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG
    # m_panel_y = screen_height - m_panel_height
    # a_panel_y = screen_height - a_panel_height - m_panel_height

    bar_width = 20
    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = m_panel_height - 1

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'white': libtcod.Color(250, 250, 250),
        'yellow': libtcod.Color(250, 250, 0)
    }

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'shop game', False)

    con = libtcod.console_new(screen_width, screen_height)
    m_panel = libtcod.console_new(panel_width, m_panel_height)
    a_panel = libtcod.console_new(panel_width, a_panel_height)

    MapManager.map = WorldMap(map_width, map_height)
    MapManager.map.make_map()

    additional_render_params = {}

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    selected_tile = (0, 0)

    additional_render_params['selected_tile'] = selected_tile
    message_log = MessageLog(message_x, message_width, message_height)
    action_panel_messages = []

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        render_all(con, m_panel, a_panel, screen_width - panel_width, 0, panel_width, a_panel_height,
                   screen_width - panel_width, a_panel_height, panel_width, m_panel_height,
                   MapManager.map, screen_width, screen_height,
                   m_panel_height, colors, additional_render_params, game_state, message_log, action_panel_messages)
        libtcod.console_flush()

        action_panel_messages = get_action_messages()
        key_action = handle_keys(key, game_state)
        selector_move = key_action.get('selector_move')
        # selector_move = key_action.get('key_1')
        action = key_action.get('action')

        if selector_move:
            selected_tile = tuple(map(operator.add, selected_tile, selector_move))
            additional_render_params['selected_tile'] = selected_tile

        clear_all(con, MapManager.map)

        if debug:
            handle_debug(MapManager.map.tiles[selected_tile[0]][selected_tile[1]], action_panel_messages, key_action)


if __name__ == '__main__':
    main()
