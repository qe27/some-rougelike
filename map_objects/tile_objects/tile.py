import global_variables
from map_objects.map_types import *
from objects.game_objects.world_map.landscape.open_sea import OpenSea


class Tile:
    """
    A tile on a map. It contains objects.
    """

    def __init__(self, upper_map, x=None, y=None, tile_object=None, lower_map=None):
        """
        TODO: support list of objects
        """
        self.upper_map = upper_map
        self.lower_map = lower_map
        self.x = x
        self.y = y
        # self.exists = exists
        self.tile_ = []
        if tile_object:
            self.tile_object = tile_object
        else:
            if self.upper_map.map_type == WORLD_MAP:
                self.tile_object = OpenSea()
            elif self.upper_map.map_type == LOCATION_MAP:
                self.tile_object = OpenSea()
        self.tile_object.tile = self

    def is_near(self, tile):
        if abs(self.x - tile.x) <= 1 and abs(self.y - tile.y) <= 1:
            return True
        return False

    def get_char(self):
        if self.tile_object:
            return self.tile_object.char

    def get_color(self):
        if self.tile_object:
            return self.tile_object.color
