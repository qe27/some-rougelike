import time

import tcod as libtcod

from map_objects.game_map import FloorMap
from objects.game_objects.worker import Worker
from render_functions import render_all, clear_all
from scripts.game_states import GameStates
from scripts.input_handlers import handle_keys
import operator
from scripts.wait_thread import WaitThread


def main():
    speed_dict = {3: 0.25, 2: 0.33, 1: 0.5, 0: 1, -1: 2, -2: 3, -3: 4}
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
    game_state = GameStates.PAUSED
    paused = False
    speed = 0

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'white': libtcod.Color(250, 250, 250),
        'yellow': libtcod.Color(250, 250, 0)
    }

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'shop game', False)

    con = libtcod.console_new(screen_width, screen_height)

    floor_map = FloorMap(map_width, map_height)
    floor_map.make_map()

    additional_render_params = {}

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    key_pressed_while_wait = {}

    selected_tile = (0, 0)

    additional_render_params['selected_tile'] = selected_tile

    # map_scripts.calculatePath(floor_map.tiles[10][10], floor_map.tiles[15][15], floor_map)

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        render_all(con, floor_map, screen_width, screen_height, colors, additional_render_params, game_state)
        libtcod.console_flush()

        # if bool(key_pressed_while_wait):
        #     key_action = key_pressed_while_wait
        #     # key_pressed_while_wait = {}
        # else:
        #      key_action = handle_keys(key, game_state)

        key_action = handle_keys(key, game_state)
        toggle_pause = key_action.get('toggle_pause')
        selector_move = key_action.get('selector_move')
        change_speed = key_action.get('change_speed')

        if toggle_pause:
            if game_state == game_state.PAUSED:
                game_state = game_state.IN_PROGRESS
            else:
                game_state = game_state.PAUSED

        if change_speed:
            speed = speed + change_speed
            if speed < -3:
                speed = -3
            if speed > 3:
                speed = 3
        change_speed = None
        # key_action = {}

        if game_state == game_state.IN_PROGRESS:
            objects_actions = {}

            for x in range(map_width):
                for y in range(map_height):
                    if floor_map.tiles[x][y].objects:
                        for obj in floor_map.tiles[x][y].objects:
                            if isinstance(obj, Worker):
                                action_result = obj.doAction()
                                # print("action result %s" % action_result)
                                objects_actions[obj] = action_result

            for obj, action in objects_actions.items():
                if isinstance(obj, Worker):
                    if action['actionResult'] == 'moving':
                        obj.setTile(floor_map.tiles[action['moveTo'][0]][action['moveTo'][1]])
            print('speed %s' % speed)
            # its essential to read keys 'during' pause because otherwise we would miss inputs
            # TODO: fix problem with key input delay
            t = 0.005
            while t < speed_dict[speed]:
                libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
                key_action = handle_keys(key, game_state)
                toggle_pause = key_action.get('toggle_pause')
                change_speed = key_action.get('change_speed')
                if toggle_pause:
                    game_state = game_state.PAUSED
                    break
                if change_speed:
                    speed = speed + change_speed
                    if speed < -3:
                        speed = -3
                    if speed > 3:
                        speed = 3
                    break
                time.sleep(0.005)
                t += 0.005
            # wait_thread = WaitThread(speed_dict[speed])
            # key_pressed_while_wait = {}
            # wait_thread.start()
            # while wait_thread.is_alive():
            # key_pressed_while_wait = handle_keys(key, GameStates.IN_PROGRESS)
            # libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
            # key_pressed_while_wait = handle_keys(key, GameStates.IN_PROGRESS)
            # if key_pressed_while_wait:
            #     pass

        else:
            if selector_move:
                selected_tile = tuple(map(operator.add, selected_tile, selector_move))
                additional_render_params['selected_tile'] = selected_tile

        clear_all(con, floor_map)


if __name__ == '__main__':
    main()
