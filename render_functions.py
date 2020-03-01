import tcod as libtcod


def render_all(con, game_map, screen_width, screen_height, colors):
    # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):

            if game_map.tiles[x][y].exists:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)

            draw_objects(con, game_map.tiles[x][y].objects)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


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