import tcod as libtcod

from map_objects.tile import Tile
from objects.game_objects.game_object import GameObject
from objects.game_objects.interactable_object import InteractableObject
from objects.game_objects.worker import Worker


class FloorMap:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(x, y) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self):
        for x in range(self.width):
            for y in range(self.height):
                if (5 < x < 25) and (5 < y < 25):
                    self.tiles[x][y].exists = True

        self.tiles[10][10].objects.append(Worker(libtcod.red, "player2", tile=self.tiles[10][10]))
        self.tiles[15][15].objects.append(Worker(libtcod.white, "player", tile=self.tiles[15][15]))
        self.tiles[17][17].objects.append(InteractableObject(libtcod.blue, "Cabinet", "C", tile=self.tiles[17][17]))
        self.tiles[18][17].objects.append(GameObject("F", libtcod.red, "fire", tile=self.tiles[18][17]))
        self.tiles[19][17].objects.append(GameObject("F", libtcod.red, "fire", tile=self.tiles[19][17]))
        self.tiles[11][11].objects.append(GameObject("F", libtcod.red, "fire", tile=self.tiles[11][11]))
        self.tiles[11][12].objects.append(GameObject("F", libtcod.red, "fire", tile=self.tiles[11][12]))
