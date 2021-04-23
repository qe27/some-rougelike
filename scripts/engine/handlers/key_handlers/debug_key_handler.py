# from map_objects.map_manager import create_test_object
from map_objects.map_manager import create_map_object
from objects.game_objects.map_object import MapObject
from rendering.render_functions import MenusRenderingState, MenusRenderingOptions
from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
from scripts.engine.handlers.key_handlers.selected_options import SelectedOptions


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
    key_2 = key_action.get('key_2')
    key_9 = key_action.get('key_9')
    key_0 = key_action.get('key_0')

    if key_9:
        # create_test_object(tile)
        # CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG
        create_map_object(tile, SelectedOptions.options)
    if key_0:
        CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG
    if key_2:
        MenusRenderingState.ACTIVE_RENDERING_STATE = MenusRenderingOptions.SELECTOR_MENU
        MenusRenderingState.OPTIONS['menu_title'] = 'Select type from list'
        MenusRenderingState.OPTIONS['options'] = [str(i.__name__) for i in MapObject.__subclasses__()]
        CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG_CREATE_SET_TYPE


def handle_select_type(key_action, tile):
    types = MapObject.__subclasses__()
    letter_index = ord('a')
    for map_object_type in types:
        if key_action.get('key_' + chr(letter_index)):
            SelectedOptions.options['map_object_type'] = map_object_type
            CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG_CREATE
            MenusRenderingState.ACTIVE_RENDERING_STATE = None
            MenusRenderingState.OPTIONS = {}
        letter_index += 1
