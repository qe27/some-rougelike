from datetime import datetime

import tcod as libtcod

from scripts.game_states import GameStates


def render_all(con, game_map, screen_width, screen_height, colors, additional_render_params, game_state):
    if game_state == GameStates.IN_PROGRESS or game_state == GameStates.PAUSED:
        # Draw all the tiles in the game map
        for y in range(game_map.height):
            for x in range(game_map.width):

                if game_map.tiles[x][y].exists:
                    libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)

                draw_objects(con, game_map.tiles[x][y].objects)
                if game_state == GameStates.PAUSED and additional_render_params['selected_tile']:
                    draw_selector(con, additional_render_params['selected_tile'], colors)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def draw_selector(con, selector, colors):
    # curr_time = datetime.now()
    if int(datetime.now().strftime('%S')) % 2 == 0:
        libtcod.console_set_char_background(con, selector[0], selector[1], colors.get('yellow'), libtcod.BKGND_SET)
        libtcod.console_put_char(con, selector[0], selector[1], 'X', libtcod.COLOR_RED)


def clear_all(con, game_map):
    for y in range(game_map.height):
        for x in range(game_map.width):
            clear_entity(con, game_map.tiles[x][y])


def draw_objects(con, objects):
    if objects:
        libtcod.console_set_default_foreground(con, objects[0].color)
        libtcod.console_put_char(con, objects[0].tile.x, objects[0].tile.y, objects[0].char, libtcod.BKGND_NONE)

def clear_entity(con, tile):
    # erase the character that represents this object
    libtcod.console_put_char(con, tile.x, tile.y, ' ', libtcod.BKGND_NONE)