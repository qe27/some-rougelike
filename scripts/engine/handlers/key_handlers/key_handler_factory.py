from scripts.engine.active_state import ActiveStates
from scripts.engine.handlers.key_handlers import debug_key_handler


def handle(active_state, key_action, tile):
    if active_state == ActiveStates.DEBUG:
        debug_key_handler.handle(key_action, tile)
    # elif active_state == ActiveStates.DEBUG_CREATE:
    #     return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']
    # elif active_state == ActiveStates.DEBUG_CREATE_SET_NAME:
    #     return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']
    # elif active_state == ActiveStates.DEBUG_CREATE_SET_TYPE:
    #     return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']
