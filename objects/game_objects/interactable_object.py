import abc

from objects.game_objects.game_object import GameObject


class InteractableObject(GameObject):

    def __init__(self, color, name, char, action=None, tile=None, endTurnAction=None, blocks=True):
        GameObject.__init__(self, char, color, name, blocks=blocks, tile=tile)
        self.action = action
        self.endTurnAction = endTurnAction


    def doEndTurnAction(self, tiles):
        if self.endTurnAction is not None:
            self.endTurnAction.action(self.tile, tiles)
