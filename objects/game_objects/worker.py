from objects.game_objects.game_object import GameObject


class Worker(GameObject):

    def __init__(self, color, name, stats=[], char='@', tile=None):
        GameObject.__init__(self, char, color, name, tile=tile)
        self.stats = stats
        self.actionChain = []
        self.currentAction = None
        self.chainCoeff = 0

    def addAction(self, action):
        self.actionChain.append(action)

    def doAction(self):
        if self.currentAction is None:
            self.currentAction = self.actionChain[0]
            self.chainCoeff = 0

        result = self.currentAction.doAction({"key": "value"})
        if result['completed']:
            if self.chainCoeff >= len(self.actionChain) - 1:
                self.chainCoeff = 0
            else:
                self.chainCoeff = self.chainCoeff + 1

            self.currentAction = self.actionChain[self.chainCoeff]
