class MapManager:
    map = None


# def create_test_object(tile):
#     tile.objects.append(MapObject('Test', 'Test Description', tcod.cyan, '@'))


def create_map_object(tile, options):
    #tile.objects.append(River(name='Nile', description='Egyptian river', color=tcod.blue, char=None, options={}))
    tile.objects.append(options.get('map_object_type')())
