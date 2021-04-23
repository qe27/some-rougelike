import tcod as libtcod
from scripts.game_states import GameStates


def handle_keys(key, game_state):
    if game_state == GameStates.IN_PROGRESS:
        return handle_in_progress_keys(key)
    elif game_state == GameStates.PAUSED:
        return handle_paused_keys(key)
    return {}


def handle_paused_keys(key):
    key_char = chr(key.c)

    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'selector_move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'selector_move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'selector_move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
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
    elif key_char == 'a':
        return {'key_a': True}
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
