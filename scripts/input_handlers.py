import tcod as libtcod

from scripts.engine.active_state import *


def handle_keys(key, game_state):
    if game_state == ActiveStates.WORLD_MAP or game_state == ActiveStates.SHIP_MAP:
        return handle_world_map_keys(key)
    return {}


def handle_world_map_keys(key):
    key_char = chr(key.c)

    if key.lctrl:
        if key.vk == libtcod.KEY_UP:
            return {'offset_move': (0, -1)}
        elif key.vk == libtcod.KEY_DOWN:
            return {'offset_move': (0, 1)}
        elif key.vk == libtcod.KEY_LEFT:
            return {'offset_move': (-1, 0)}
        elif key.vk == libtcod.KEY_RIGHT:
            return {'offset_move': (1, 0)}

    if key.vk == libtcod.KEY_UP:
        return {'selector_move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'selector_move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'selector_move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'selector_move': (1, 0)}
    elif key.vk == libtcod.KEY_KPADD:
        return {'change_speed': 1}
    elif key.vk == libtcod.KEY_KPSUB:
        return {'change_speed': -1}
    elif key.vk == libtcod.KEY_SPACE:
        return {'toggle_pause': True}
    elif key.vk == libtcod.KEY_ENTER:
        return {'action': True}
    elif key.vk == libtcod.KEY_1:
        return {'key_1': True}
    elif key.vk == libtcod.KEY_2:
        return {'key_2': True}
    elif key.vk == libtcod.KEY_3:
        return {'key_3': True}
    elif key.vk == libtcod.KEY_4:
        return {'key_4': True}
    elif key.vk == libtcod.KEY_5:
        return {'key_5': True}
    elif key.vk == libtcod.KEY_6:
        return {'key_6': True}
    elif key.vk == libtcod.KEY_7:
        return {'key_7': True}
    elif key.vk == libtcod.KEY_8:
        return {'key_8': True}
    elif key.vk == libtcod.KEY_9:
        return {'key_9': True}
    elif key.vk == libtcod.KEY_0:
        return {'key_0': True}
    # elif key_char == 'a':
    elif key_char:
        return {'key_' + key_char: True}
    # elif key.vk == libtcod.KEY_b:
    #     return {'key_a': True}
    # elif key.vk == libtcod.KEY_a:
    #     return {'key_a': True}
    # elif key.vk == libtcod.KEY_a:
    #     return {'key_a': True}
    # elif key.vk == libtcod.KEY_a:
    #     return {'key_a': True}

    return {}


def handle_in_progress_keys(key):
    if key.vk == libtcod.KEY_SPACE:
        return {'toggle_pause': True}
    elif key.vk == libtcod.KEY_KPADD:
        return {'change_speed': 1}
    elif key.vk == libtcod.KEY_KPSUB:
        return {'change_speed': -1}
    elif key.vk == libtcod.KEY_ENTER:
        return {'action': True}

    return {}
