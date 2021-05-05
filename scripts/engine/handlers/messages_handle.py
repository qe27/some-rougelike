from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
from scripts.engine.handlers.key_handlers.selected_options import SelectedOptions


def get_action_messages():
    active_state = CurrentActiveState.ACTIVE_STATE
    if active_state in [ActiveStates.WORLD_MAP, ActiveStates.LOCATION_MAP]:
        return ['No Messages!']
    elif active_state == ActiveStates.DEBUG_CREATE:
        object_type = SelectedOptions.options.get('map_object_type')
        terrain_object = SelectedOptions.options.get('selected_terrain_object')
        object_type_message = '2 - Set type'
        terrain_object_message = '3 - Select terrain object'
        if object_type:
            object_type_message = '2 - Set type: ' + object_type.type
        if terrain_object:
            terrain_object_message = '3 - terrain object: ' + terrain_object.type
        return ['1 - Set name', object_type_message, terrain_object_message, '9 - Create',
                '0 - Cancel']
    elif active_state == ActiveStates.DEBUG_CREATE_SET_NAME:
        return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']
    elif active_state == ActiveStates.DEBUG_CREATE_SET_TYPE:
        return ['1 - Set name', '2 - Set type', '9 - Create', '0 - Cancel']