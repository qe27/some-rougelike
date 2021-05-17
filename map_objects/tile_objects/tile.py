from datetime import datetime

import global_variables
from map_objects.map_types import *
from objects.game_objects.world_map.landscape.open_sea import OpenSea
from objects.game_objects.world_map.landscape.static_landscape_objects import open_sea


class Tile:
    """
    A tile on a map. It contains objects.
    """

    def __init__(self, upper_map, x=None, y=None, landscape=None, lower_map=None):
        """
        TODO: support list of objects
        """
        self.upper_map = upper_map
        self.lower_map = lower_map
        self.x = x
        self.y = y
        # self.exists = exists
        self.tile_ = []
        if landscape:
            self.landscape = landscape
        else:
            if self.upper_map.map_type == WORLD_MAP:
                self.landscape = open_sea
            elif self.upper_map.map_type == LOCATION_MAP:
                self.landscape = open_sea
        self.landscape.tile = self
        self.objects = []

    def is_near(self, tile):
        if abs(self.x - tile.x) <= 1 and abs(self.y - tile.y) <= 1:
            return True
        return False

    def get_char(self):
        if self.landscape:
            if len(self.objects) == 0:
                return self.landscape.char
            else:
                if int(datetime.now().strftime('%S')) % 2 == 0:
                    return self.objects[0].char
                else:
                    return self.landscape.char

    def get_color(self):
        if self.landscape:
            if len(self.objects) == 0:
                return self.landscape.color
            else:
                if int(datetime.now().strftime('%S')) % 2 == 0:
                    return self.objects[0].color
                else:
                    return self.landscape.color
