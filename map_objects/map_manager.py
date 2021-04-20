import tcod

from objects.game_objects.map_object import MapObject


class MapManager:
    map = None


def create_test_object(tile):
    tile.objects.append(MapObject('Test', 'Test Description', tcod.cyan, '@'))
