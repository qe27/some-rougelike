from datetime import datetime
from enum import Enum

import tcod as libtcod
from tcod import console_set_default_background

import global_variables
from global_variables import *
from rendering.menus import selector_menu
from rendering.screen_options import *
from scripts.engine.active_state import ActiveStates
from scripts.engine.handlers import options_manager
from scripts.game_states import GameStates


class MenusRenderingState:
    ACTIVE_RENDERING_STATE = None
    OPTIONS = {"draw_end_turn_button": True}


class MenusRenderingOptions(Enum):
    SELECTOR_MENU = 1


m_panel = libtcod.console_new(PANEL_WIDTH, M_PANEL_HEIGHT)
a_panel = libtcod.console_new(PANEL_WIDTH, A_PANEL_HEIGHT)
info_panel = libtcod.console_new(SCREEN_WIDTH - PANEL_WIDTH, SCREEN_HEIGHT - MAIN_PANEL_HEIGHT)

colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'white': libtcod.Color(250, 250, 250),
        'yellow': libtcod.Color(250, 250, 0),
        'gray': libtcod.gray,
        'brown': libtcod.Color(70, 20, 20)
    }

opposite_colors = {
    'gray': libtcod.white,
    'brown': libtcod.white
}

def render_all(game_state, action_panel_messages, messages_panel=m_panel,
               action_panel=a_panel, action_panel_x=SCREEN_WIDTH - PANEL_WIDTH,
               action_panel_y=0, action_panel_width=PANEL_WIDTH,
               action_panel_height=A_PANEL_HEIGHT,
               messages_panel_x=SCREEN_WIDTH - PANEL_WIDTH,
               messages_panel_y=A_PANEL_HEIGHT,
               messages_panel_width=PANEL_WIDTH, messages_panel_height=M_PANEL_HEIGHT,
               con=global_variables.CONSOLE, screen_width=SCREEN_WIDTH,
               screen_height=SCREEN_HEIGHT):
    game_map = global_variables.get_current_map()
    if game_state == ActiveStates.WORLD_MAP or game_state == ActiveStates.LOCATION_MAP:
        # Draw all the tiles in the game map
        for y in range(min(game_map.height, MAIN_PANEL_HEIGHT)):
            for x in range(min(game_map.width, MAIN_PANEL_WIDTH)):
                libtcod.console_set_char_background(con, x, y, libtcod.Color(15, 15, 15), libtcod.BKGND_SET)
                # if game_map.tiles[x][y].exists:
                #     libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
                # else:
                #     libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                draw_objects(con, game_map, game_map.tiles[x + game_map.map_offset[0]][y + game_map.map_offset[1]])
        if game_map.selected_tile:
            draw_selector(con, game_map.selected_tile, colors, game_map)

    elif game_state == ActiveStates.SHIP_MAP:
        # Draw selected ship layer
        ship = global_variables.player.ship
        layer_to_render = ship.model.get(global_variables.selected_ship_layer)
        for y in range(MAIN_PANEL_HEIGHT):
            for x in range(MAIN_PANEL_WIDTH):
                if ((0 <= x < (MAIN_PANEL_WIDTH - len(layer_to_render.tiles[0]))/2 or (MAIN_PANEL_WIDTH + len(layer_to_render.tiles[0]))/2  <= x < MAIN_PANEL_WIDTH) or
                        (0 <= y < (MAIN_PANEL_HEIGHT - len(layer_to_render.tiles))/2 or (MAIN_PANEL_HEIGHT + len(layer_to_render.tiles))/2  <= y < MAIN_PANEL_HEIGHT)):
                    libtcod.console_set_char_background(con, x, y, libtcod.Color(15, 15, 15), libtcod.BKGND_SET)
                    # libtcod.console_set_default_foreground(con, opposite_colors.get(tile.material.get('color')))
                    libtcod.console_put_char(con, x, y, ' ', libtcod.BKGND_DEFAULT)
                else:
                    tile = layer_to_render.tiles[int(y - (MAIN_PANEL_HEIGHT - len(layer_to_render.tiles))/2)][int(x - (MAIN_PANEL_WIDTH - len(layer_to_render.tiles[0]))/2)]
                    if tile.type and tile.material:
                        libtcod.console_set_char_background(con, x, y, colors.get(tile.material.get('color')), libtcod.BKGND_SET)
                        libtcod.console_set_default_foreground(con, opposite_colors.get(tile.material.get('color')))
                        libtcod.console_put_char(con, x, y, tile.type.get('character'), libtcod.BKGND_DEFAULT)
                    else:
                        libtcod.console_set_char_background(con, x, y, libtcod.azure, libtcod.BKGND_SET)
                        libtcod.console_put_char(con, x, y, ' ', libtcod.BKGND_DEFAULT)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

    if game_map.selected_tile:
        messages_panel.clear()
        console_set_default_background(messages_panel, libtcod.Color(15, 15, 15))
        draw_tile_info(messages_panel,
                       game_map.tiles[game_map.selected_tile[0]][game_map.selected_tile[1]])
        libtcod.console_blit(messages_panel, 0, 0, messages_panel_width, messages_panel_height, 0, messages_panel_x,
                             messages_panel_y)

    action_panel.clear()

    draw_subject_functions(action_panel)
    # y = 1
    # for message in action_panel_messages:
    #     console_set_default_background(action_panel, libtcod.gray)
    #     libtcod.console_set_default_foreground(action_panel, libtcod.white)
    #     libtcod.console_print_ex(action_panel, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, message)
    #     y += 1

    libtcod.console_blit(action_panel, 0, 0, action_panel_width, action_panel_height, 0, action_panel_x, action_panel_y)

    info_panel.clear()
    console_set_default_background(info_panel, libtcod.azure)
    if game_map.selected_tile:
        draw_selected_object_functions(info_panel)

    libtcod.console_blit(info_panel, 0, 0, SCREEN_WIDTH - PANEL_WIDTH, SCREEN_HEIGHT - MAIN_PANEL_HEIGHT, 0, 0,
                         MAIN_PANEL_HEIGHT)

    # if MenusRenderingState.ACTIVE_RENDERING_STATE == MenusRenderingOptions.SELECTOR_MENU:
    #     selector_menu(con, MenusRenderingState.OPTIONS.get('menu_title'), MenusRenderingState.OPTIONS.get('options'),
    #                   50)

    end_turn_button = libtcod.console_new(10, 3)
    if MenusRenderingState.OPTIONS.get("draw_end_turn_button"):
        draw_end_turn_button(end_turn_button)
        libtcod.console_blit(end_turn_button, 0, 0, 10, 3, 0, screen_width - 10,
                             screen_height - 3)


def draw_selected_object_functions(con):
    # return
    global_variables.object_options = {}
    y = 0
    for option in options_manager.get_selected_object_functions().items():
        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_print_ex(con, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, option[0])
        global_variables.object_options[y] = option[1]
        y += 1

def draw_subject_functions(con):
    y = 0
    global_variables.subject_options = {}
    for option in options_manager.get_subject_functions().items():
        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_print_ex(con, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, option[0])
        global_variables.subject_options[y] = option[1]
        y += 1

def draw_tile_info(con, tile):
    return
    # y = 0
    # for item_to_print in tile.get_tile_info_to_print():
    #     libtcod.console_set_default_foreground(con, item_to_print[2])
    #     libtcod.console_print_ex(con, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, item_to_print[1])
    #     global_variables.tile_info_options[y] = item_to_print[0]
    #     y += 1


def draw_end_turn_button(con):
    for x in range(0, 10):
        for y in range(0, 3):
            libtcod.console_set_char_background(con, x, y, libtcod.Color(250, 250, 0), libtcod.BKGND_SET)
    libtcod.console_set_default_foreground(con, libtcod.black)
    libtcod.console_print_ex(con, 1, 1, libtcod.BKGND_NONE, libtcod.LEFT, 'END TURN')


def draw_selector(con, selector, colors, current_map):
    # curr_time = datetime.now()
    if int(datetime.now().strftime('%S')) % 2 == 0:
        libtcod.console_set_char_background(con, selector[0] - current_map.map_offset[0], selector[1] - current_map.map_offset[1], colors.get('yellow'), libtcod.BKGND_SET)
        libtcod.console_put_char(con, selector[0] - current_map.map_offset[0], selector[1] - current_map.map_offset[1], 'X', libtcod.COLOR_RED)


def clear_all(con, game_state):
    current_map = global_variables.get_current_map()
    for y in range(min(current_map.height, MAIN_PANEL_HEIGHT)):
        for x in range(min(current_map.width, MAIN_PANEL_WIDTH)):
            if game_state == ActiveStates.WORLD_MAP:
                clear_entity(con, current_map, current_map.tiles[x + current_map.map_offset[0]][y + current_map.map_offset[1]])
            elif game_state == ActiveStates.SHIP_MAP:
                libtcod.console_put_char(con, x, y, ' ', libtcod.BKGND_NONE)


def draw_objects(con, current_map, tile):
    libtcod.console_set_default_foreground(con, tile.get_color())
    libtcod.console_put_char(con, tile.x - current_map.map_offset[0], tile.y - current_map.map_offset[1], tile.get_char(), libtcod.BKGND_NONE)


def clear_entity(con, current_map, tile):
    # erase the character that represents this object
    libtcod.console_put_char(con, tile.x - current_map.map_offset[0], tile.y - current_map.map_offset[1], ' ', libtcod.BKGND_NONE)
