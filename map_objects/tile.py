from map_objects.map_manager import MapManager
from objects.game_objects.tile_structure import TileStructure


class Tile:
    """
    A tile on a map. It contains objects.
    """

    def __init__(self, game_map=MapManager.map, x=None, y=None, tile_structure=None):
        """
        TODO: support list of objects
        """
        self.game_map = game_map
        self.x = x
        self.y = y
        # self.exists = exists
        self.tile_ = []
        if tile_structure:
            self.tile_structure = tile_structure
        else:
            self.tile_structure = TileStructure()
        self.tile_structure.tile = self

    def is_near(self, tile):
        if abs(self.x - tile.x) <= 1 and abs(self.y - tile.y) <= 1:
            return True
        return False

    def get_char(self):
        if self.tile_structure:
            return self.tile_structure.get_prior_object().char

    def get_color(self):
        if self.tile_structure:
            return self.tile_structure.get_prior_object().color

    def get_landscape_objects(self):
        if self.tile_structure:
            return list(self.tile_structure.landscape.keys())
