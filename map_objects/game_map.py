import tcod as libtcod

from map_objects.tile import Tile


class WorldMap:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(self, x, y) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self):
        for x in range(self.width):
            for y in range(self.height):
                if (5 < x < 25) and (5 < y < 25):
                    self.tiles[x][y].exists = True

        # for test purposes
        # self.prepare_test_requisites()
        # self.tiles[17][17].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[17][17]))