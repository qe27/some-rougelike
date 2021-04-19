from map_objects.map_manager import MapManager


class Tile:
    """
    A tile on a map. It contains objects.
    """

    def __init__(self, game_map=MapManager.map, x=None, y=None, game_object=None):
        """
        TODO: support list of objects
        """
        self.game_map = game_map
        self.x = x
        self.y = y
        # self.exists = exists
        self.objects = []
        if game_object is not None:
            self.objects.append(game_object)
        #    game_object.tile = self

    def isNear(self, tile):
        if abs(self.x - tile.x) <= 1 and abs(self.y - tile.y) <= 1:
            return True
        return False

    def getChar(self):
        if self.objects:
            return self.objects[0].char

    def getColor(self):
        if self.objects:
            return self.objects[0].color
