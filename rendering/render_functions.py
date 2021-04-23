from datetime import datetime
from enum import Enum

import tcod as libtcod

from rendering.menus import selector_menu
from scripts.game_states import GameStates


class MenusRenderingState:
    ACTIVE_RENDERING_STATE = None
    OPTIONS = {}


class MenusRenderingOptions(Enum):
    SELECTOR_MENU = 1


def render_all(con, messages_panel, action_panel, action_panel_x, action_panel_y, action_panel_width,
               action_panel_height, messages_panel_x, messages_panel_y, messages_panel_width, messages_panel_height,
               game_map, screen_width, screen_height, panel_height, colors,
               additional_render_params, game_state, message_log, action_panel_messages):
    if game_state == GameStates.IN_PROGRESS or game_state == GameStates.PAUSED:
        # Draw all the tiles in the game map
        for y in range(game_map.height):
            for x in range(game_map.width):
                libtcod.console_set_char_background(con, x, y, libtcod.Color(15, 15, 15), libtcod.BKGND_SET)
                # if game_map.tiles[x][y].exists:
                #     libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
                # else:
                #     libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)

                draw_objects(con, game_map.tiles[x][y])
                if game_state == GameStates.PAUSED and additional_render_params['selected_tile']:
                    draw_selector(con, additional_render_params['selected_tile'], colors)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

    messages_panel.clear()

    y = 1
    for message in message_log.messages:
        libtcod.console_set_default_foreground(messages_panel, message.color)
        libtcod.console_print_ex(messages_panel, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
        y += 1

    libtcod.console_blit(messages_panel, 0, 0, messages_panel_width, messages_panel_height, 0, messages_panel_x, messages_panel_y)

    action_panel.clear()

    y = 1
    for message in action_panel_messages:
        libtcod.console_set_default_foreground(action_panel, libtcod.purple)
        libtcod.console_print_ex(action_panel, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, message)
        y += 1

    libtcod.console_blit(action_panel, 0, 0, action_panel_width, action_panel_height, 0, action_panel_x, action_panel_y)

    if MenusRenderingState.ACTIVE_RENDERING_STATE == MenusRenderingOptions.SELECTOR_MENU:
        selector_menu(con, MenusRenderingState.OPTIONS.get('menu_title'), MenusRenderingState.OPTIONS.get('options'), 50, screen_width, screen_height)


def draw_selector(con, selector, colors):
    # curr_time = datetime.now()
    if int(datetime.now().strftime('%S')) % 2 == 0:
        libtcod.console_set_char_background(con, selector[0], selector[1], colors.get('yellow'), libtcod.BKGND_SET)
        libtcod.console_put_char(con, selector[0], selector[1], 'X', libtcod.COLOR_RED)


def clear_all(con, game_map):
    for y in range(game_map.height):
        for x in range(game_map.width):
            clear_entity(con, game_map.tiles[x][y])


def draw_objects(con, tile):
    if tile.objects:
        libtcod.console_set_default_foreground(con, tile.getColor())
        libtcod.console_put_char(con, tile.x, tile.y, tile.getChar(), libtcod.BKGND_NONE)

def clear_entity(con, tile):
    # erase the character that represents this object
    libtcod.console_put_char(con, tile.x, tile.y, ' ', libtcod.BKGND_NONE)