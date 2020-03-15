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

    return {}


def handle_in_progress_keys(key):
    if key.vk == libtcod.KEY_SPACE:
        return {'toggle_pause': True}
    elif key.vk == libtcod.KEY_KPADD:
        return {'change_speed': 1}
    elif key.vk == libtcod.KEY_KPSUB:
        return {'change_speed': -1}

    return {}
