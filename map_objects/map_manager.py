class MapManager:
    map = None


def create_map_object(tile_structure, options):
    structure = options.get('map_object_type')()
    landscape_object = options.get('selected_landscape_object')
    structure.map_object = landscape_object
    landscape_object.structures.append(structure)
