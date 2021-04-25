# from map_objects.map_manager import create_test_object
from map_objects.map_manager import create_map_object, create_resource_source
from objects.game_objects.map_object import MapObject
from objects.game_objects.resources.resources_types import RESOURCES_DICT
from objects.game_objects.structures.structure import Structure
from rendering import menus
from rendering.menus import menu
from rendering.render_functions import MenusRenderingState, MenusRenderingOptions
from scripts.engine.active_state import ActiveStates
from scripts.engine.current_active_state import CurrentActiveState
from scripts.engine.handlers.key_handlers.selected_options import SelectedOptions


def handle(key_action, tile):
    key_1 = key_action.get('key_1')
    key_2 = key_action.get('key_2')
    key_3 = key_action.get('key_3')

    # if tile.objects:
    #     if key_2:
    #         del tile.objects[0]
    if key_1:
        CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG_CREATE
    if key_2:
        # available_tile_terrains = tile.get_terrain_objects
        selected_option = menu('Select terrain object', list(map(lambda x: x.type, tile.get_terrain_objects())), 50)
        if selected_option is None:
            return
        selected_terrain = tile.get_terrain_objects()[selected_option]
        available_resource_types = list(RESOURCES_DICT.keys())
        selected_option = menu('Select resource type', available_resource_types, 50)
        if selected_option is None:
            return
        selected_resource_type = available_resource_types[selected_option]
        created_source = create_resource_source(selected_terrain, selected_resource_type)
        print('Created resource source with type :' + created_source.resource_type + 'on tile : ' +
              str(created_source.terrain.tile_structure.tile.x) + ',' + str(created_source.terrain.tile_structure.tile.y))


def handle_create(key_action, tile):
    #add edit field
    key_1 = key_action.get('key_1')
    key_2 = key_action.get('key_2')
    key_3 = key_action.get('key_3')
    key_9 = key_action.get('key_9')
    key_0 = key_action.get('key_0')

    if SelectedOptions.options.get('selected_terrain_object') \
            and SelectedOptions.options.get('selected_terrain_object').tile_structure.tile != tile:
        if len(tile.tile_structure.terrain) == 1:
            SelectedOptions.options['selected_terrain_object'] = list(tile.tile_structure.terrain.keys())[0]
        else:
            SelectedOptions.options['selected_terrain_object'] = None

    if SelectedOptions.options.get('selected_terrain_object') is None and len(tile.tile_structure.terrain) == 1:
        if len(tile.tile_structure.terrain) == 1:
            SelectedOptions.options['selected_terrain_object'] = list(tile.tile_structure.terrain.keys())[0]

    if key_3:
        terrain = tile.get_terrain_objects()
        selected_option = menu('Select map object', [i.type for i in terrain], 50)
        if selected_option is None:
            CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG
        else:
            SelectedOptions.options['selected_terrain_object'] = terrain[selected_option]

    if key_9:
        # add validation
        create_map_object(tile.tile_structure, SelectedOptions.options)
    if key_0:
        CurrentActiveState.ACTIVE_STATE = ActiveStates.DEBUG
    if key_2:
        classes = Structure.__subclasses__()
        index_to_classes_map = {i: classes[i] for i in range(0, len(classes))}
        SelectedOptions.options['map_object_type'] = index_to_classes_map.get(
            menu('Select Type', [str(i.__name__) for i in classes], 50))


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
