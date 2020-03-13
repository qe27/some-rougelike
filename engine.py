import time

import tcod as libtcod

from map_objects.game_map import FloorMap
from objects.game_objects.worker import Worker
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

    # map_scripts.calculatePath(floor_map.tiles[10][10], floor_map.tiles[15][15], floor_map)

    while not libtcod.console_is_window_closed():
        render_all(con, floor_map, screen_width, screen_height, colors)
        libtcod.console_flush()

        objects_actions = {}

        for x in range(map_width):
            for y in range(map_height):
                if floor_map.tiles[x][y].objects:
                    for obj in floor_map.tiles[x][y].objects:
                        if isinstance(obj, Worker):
                            action_result = obj.doAction()
                            print("action result %s" % action_result)
                            objects_actions[obj] = action_result

        for obj, action in objects_actions.items():
            if isinstance(obj, Worker):
                if action['actionResult'] == 'moving':
                    obj.setTile(floor_map.tiles[action['moveTo'][0]][action['moveTo'][1]])

        time.sleep(1)

        clear_all(con, floor_map)


if __name__ == '__main__':
     main()