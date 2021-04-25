from objects.game_objects.landscape.plain import Plain


class TileStructure:
    default_area = 1000

    def __init__(self, tile=None, terrain=None):
        if terrain is None:
            terrain = {Plain(): 1}
        self.tile = tile
        self.terrain = terrain
        for key in self.terrain:
            key.tile_structure = self

    def get_prior_object(self):
        max_part = 0
        prior_object = None
        for map_object, tile_part in self.terrain.items():
            if max_part < tile_part:
                max_part = tile_part
                prior_object = map_object
        if prior_object.structures:
            return prior_object.structures[0]
        return prior_object

    def get_structures(self):
        objects = []
        for terrain in self.terrain.keys():
            objects.extend(terrain.structures)
        return objects

    def set_landscape(self, terrain):
        if terrain:
            self.terrain = terrain
            for key in self.terrain.keys():
                key.tile_structure = self
