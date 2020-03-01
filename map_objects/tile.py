class Tile:
    """
    A tile on a map. It contains objects.
    """

    def __init__(self, x, y, exists=False, game_object=None):
        """
        TODO: support list of objects
        """
        self.x = x
        self.y = y
        self.exists = exists
        self.objects = []
        if game_object is not None:
            self.objects.append(game_object)
            game_object.tile = self
