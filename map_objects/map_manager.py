from objects.game_objects.resources.resource_source import ResourceSource


class MapManager:
    map = None


def create_map_object(tile_structure, options):
    structure = options.get('map_object_type')()
    terrain_object = options.get('selected_terrain_object')
    structure.map_object = terrain_object
    terrain_object.structures.append(structure)


def create_resource_source(terrain, resource_type):
    resource_source = ResourceSource(resource_type=resource_type, terrain=terrain)
    terrain.resource_sources.append(resource_source)
    return resource_source
