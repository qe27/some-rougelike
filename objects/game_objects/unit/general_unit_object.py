from objects.game_objects.actionmanager import ActionManager
from objects.game_objects.game_object import GameObject


class GeneralUnitObject(ActionManager, GameObject):

    def __init__(self, color, name, bodyState, char='@', tile=None):
        GameObject.__init__(self, char, color, name, blocks=False, tile=tile)
        ActionManager.__init__(self)
        self.bodyState = bodyState


