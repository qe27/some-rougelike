from objects.game_objects.landscape.plain import Plain


class TileStructure:
    default_area = 1000

    def __init__(self, tile=None, landscape=None):
        if landscape is None:
            landscape = {Plain(): 1}
        self.tile = tile
        self.landscape = landscape
        for key in self.landscape:
            key.tile_structure = self

    def get_prior_object(self):
        max_part = 0
        prior_object = None
        for map_object, tile_part in self.landscape.items():
            if max_part < tile_part:
                max_part = tile_part
                prior_object = map_object
        if prior_object.structures:
            return prior_object.structures[0]
        return prior_object

    def get_structures(self):
        objects = []
        for landscape in self.landscape.keys():
            objects.extend(landscape.structures)
        return objects

    def set_landscape(self, landscape):
        if landscape:
            self.landscape = landscape
            for key in self.landscape.keys():
                key.tile_structure = self
