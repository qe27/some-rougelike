from objects.game_objects.game_object import GameObject


class InteractableObject(GameObject):

    def __init__(self, color, name, char, action=None, tile=None):
        GameObject.__init__(self, char, color, name, tile=tile)
        self.action = action