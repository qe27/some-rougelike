class Tile:
    """
    A tile on a map. It contains objects.
    """

    def __init__(self, game_map, x, y, exists=False, game_object=None):
        """
        TODO: support list of objects
        """
        self.game_map = game_map
        self.x = x
        self.y = y
        self.exists = exists
        self.objects = []
        if game_object is not None:
            self.objects.append(game_object)
            game_object.tile = self

    def isNear(self, tile):
        if abs(self.x - tile.x) <= 1 and abs(self.y - tile.y) <= 1:
            return True
        return False
