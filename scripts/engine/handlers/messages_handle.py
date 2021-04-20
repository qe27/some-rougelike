from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState


def get_action_messages():
    active_state = CurrentActiveState.ACTIVE_STATE
    if active_state == ActiveStates.DEBUG:
        return ['No Messages!']
    elif active_state == ActiveStates.DEBUG_CREATE:
        return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']
    elif active_state == ActiveStates.DEBUG_CREATE_SET_NAME:
        return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']
    elif active_state == ActiveStates.DEBUG_CREATE_SET_TYPE:
        return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']