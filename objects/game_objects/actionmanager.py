from objects.game_objects.game_object import GameObject
from scripts import map_scripts


class ActionManager:

    def __init__(self):
        # GameObject.__init__(self, char, color, name, blocks=False, tile=tile)
        # if stats is None:
        #     stats = []
        # self.stats = stats
        self.actionChain = []
        self.currentAction = None
        self.chainCoeff = 0
        self.currentUnits = 0

    def addAction(self, action):
        self.actionChain.append(action)

    def doAction(self):
        if self.currentAction is None:
            self.currentAction = self.actionChain[0]
            self.chainCoeff = 0

        if self.tile.isNear(self.currentAction.interactableObject.tile):
            result = self.currentAction.doAction()
            if result['completed']:
                result['actionResult'] = 'Completed'
                if self.chainCoeff >= len(self.actionChain) - 1:
                    self.chainCoeff = 0
                else:
                    self.chainCoeff = self.chainCoeff + 1

                self.currentAction = self.actionChain[self.chainCoeff]
            else:
                result['actionResult'] = 'Not completed'
        else:
            # move to tile
            path = map_scripts.calculatePath(self.tile, self.currentAction.interactableObject.tile, self.tile.game_map)
            if path:
                result = {"actionResult": "moving",
                          "moveTo": path[1]}
            else:
                result = {"actionResult": "error"}
        return result
