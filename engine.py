import tcod as libtcod

from map_objects.game_map import FloorMap
from render_functions import render_all, clear_all
from scripts import map_scripts


def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'shop game', False)

    con = libtcod.console_new(screen_width, screen_height)

    floor_map = FloorMap(map_width, map_height)
    floor_map.make_map()

    map_scripts.calculatePath(floor_map.tiles[7][11], floor_map.tiles[15][15], floor_map)

    while not libtcod.console_is_window_closed():
        render_all(con, floor_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        clear_all(con, floor_map)


if __name__ == '__main__':
     main()