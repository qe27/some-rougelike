import tcod

from objects.game_objects.map_object import MapObject
from objects.game_objects.settlements.settlement import Settlement


class MapManager:
    map = None


# def create_test_object(tile):
#     tile.objects.append(MapObject('Test', 'Test Description', tcod.cyan, '@'))


def create_map_object(tile, options):
    map_object_type = options.get('map_object_type')
    if map_object_type == Settlement.__name__:
        tile.objects.append(Settlement(name='Test', description='Test Description', color=tcod.cyan, char=None, options={}))