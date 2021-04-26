from datetime import datetime
from enum import Enum

import tcod as libtcod

import global_variables
from global_variables import *
from map_objects.map_manager import MapManager
from rendering.menus import selector_menu
from rendering.screen_options import *
from scripts.game_states import GameStates


class MenusRenderingState:
    ACTIVE_RENDERING_STATE = None
    OPTIONS = {"draw_end_turn_button": True}


class MenusRenderingOptions(Enum):
    SELECTOR_MENU = 1


m_panel = libtcod.console_new(PANEL_WIDTH, M_PANEL_HEIGHT)
a_panel = libtcod.console_new(PANEL_WIDTH, A_PANEL_HEIGHT)
info_panel = libtcod.console_new(PANEL_WIDTH, A_PANEL_HEIGHT)


def render_all(colors, game_state, action_panel_messages, messages_panel=m_panel,
               action_panel=a_panel, action_panel_x=SCREEN_WIDTH - PANEL_WIDTH,
               action_panel_y=0, action_panel_width=PANEL_WIDTH,
               action_panel_height=A_PANEL_HEIGHT,
               messages_panel_x=SCREEN_WIDTH - PANEL_WIDTH,
               messages_panel_y=A_PANEL_HEIGHT,
               messages_panel_width=PANEL_WIDTH, messages_panel_height=M_PANEL_HEIGHT,
               con=global_variables.CONSOLE, game_map=MapManager.map, screen_width=SCREEN_WIDTH,
               screen_height=SCREEN_HEIGHT):
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
                if game_state == GameStates.PAUSED and global_variables.selected_tile:
                    draw_selector(con, global_variables.selected_tile, colors)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

    if global_variables.selected_tile:
        messages_panel.clear()
        draw_tile_info(messages_panel,
                       game_map.tiles[global_variables.selected_tile[0]][global_variables.selected_tile[1]])
        libtcod.console_blit(messages_panel, 0, 0, messages_panel_width, messages_panel_height, 0, messages_panel_x,
                             messages_panel_y)

    action_panel.clear()

    y = 1
    for message in action_panel_messages:
        libtcod.console_set_default_foreground(action_panel, libtcod.purple)
        libtcod.console_print_ex(action_panel, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, message)
        y += 1

    libtcod.console_blit(action_panel, 0, 0, action_panel_width, action_panel_height, 0, action_panel_x, action_panel_y)

    if global_variables.selected_object:
        info_panel.clear()
        draw_object_info(info_panel, global_variables.selected_object.get_object_description())
        libtcod.console_blit(info_panel, 0, 0, messages_panel_width, messages_panel_height, 0, 0,
                             game_map.height)

    # if MenusRenderingState.ACTIVE_RENDERING_STATE == MenusRenderingOptions.SELECTOR_MENU:
    #     selector_menu(con, MenusRenderingState.OPTIONS.get('menu_title'), MenusRenderingState.OPTIONS.get('options'),
    #                   50)

    end_turn_button = libtcod.console_new(10, 3)
    if MenusRenderingState.OPTIONS.get("draw_end_turn_button"):
        draw_end_turn_button(end_turn_button)
        libtcod.console_blit(end_turn_button, 0, 0, 10, 3, 0, screen_width - 10,
                             screen_height - 3)


def draw_object_info(con, options):
    y = 0
    for option in options.items():
        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_print_ex(con, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, option[0])
        global_variables.object_options[y] = option[1]
        y += 1


def draw_tile_info(con, tile):
    y = 0
    for item_to_print in tile.get_tile_info_to_print():
        libtcod.console_set_default_foreground(con, item_to_print[2])
        libtcod.console_print_ex(con, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, item_to_print[1])
        global_variables.tile_info_options[y] = item_to_print[0]
        y += 1


def draw_end_turn_button(con):
    for x in range(0, 10):
        for y in range(0, 3):
            libtcod.console_set_char_background(con, x, y, libtcod.Color(250, 250, 0), libtcod.BKGND_SET)
    libtcod.console_set_default_foreground(con, libtcod.black)
    libtcod.console_print_ex(con, 1, 1, libtcod.BKGND_NONE, libtcod.LEFT, 'END TURN')


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
    libtcod.console_set_default_foreground(con, tile.get_color())
    libtcod.console_put_char(con, tile.x, tile.y, tile.get_char(), libtcod.BKGND_NONE)


def clear_entity(con, tile):
    # erase the character that represents this object
    libtcod.console_put_char(con, tile.x, tile.y, ' ', libtcod.BKGND_NONE)
