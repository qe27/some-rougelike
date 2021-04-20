from map_objects.map_manager import create_test_object
from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState


def handle(key_action, tile):
    key_1 = key_action.get('key_1')
    key_2 = key_action.get('key_2')
    key_3 = key_action.get('key_3')

    if tile.objects:
        if key_2:
            del tile.objects[0]
    if key_1:
        CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG_CREATE


def handle_create(key_action, tile):
    key_1 = key_action.get('key_1')
    key_9 = key_action.get('key_9')
    key_0 = key_action.get('key_0')

    if key_9:
        create_test_object(tile)
        # CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG
    if key_0:
        CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG

