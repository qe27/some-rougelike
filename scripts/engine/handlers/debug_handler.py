from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
from scripts.engine.handlers.key_handlers.debug_key_handler import handle, handle_create, handle_select_type


def handle_debug(tile, action_panel_messages, key_action):
    # if action:
    if CurrentActiveState.ACTIVE_STATE == ActiveStates.DEBUG:
        if tile.objects:
            action_panel_messages[:] = ['1 - Add object', '2 - Remove object']
        else:
            action_panel_messages[:] = ['1 - Add object']
        handle(key_action, tile)
    elif CurrentActiveState.ACTIVE_STATE == ActiveStates.DEBUG_CREATE:
        handle_create(key_action, tile)
    elif CurrentActiveState.ACTIVE_STATE == ActiveStates.DEBUG_CREATE_SET_TYPE:
        handle_select_type(key_action, tile)