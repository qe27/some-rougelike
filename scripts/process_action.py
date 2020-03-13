

class ProcessAction:
    def __init__(self, interactableObject, inputTypes={}, outputTypes={}, usedSkills={}, minSkillsReqierements={}, complexity=1000, baseUnits=100):
        # imagine the following situation: you produce steel.
        # in the input types there are: {"iron": 1, "coal": 10, "pigIron": 1}
        # in the output types there are {"steel": 2, "someMetalShitWaste": 3}
        # in the used skills there are: {"strength":{"min": 1, "modifier"=0.1}, "furnaceOperating":{"min": 3, "modifier": 0.3}, "steelProducing":{"min":5, "modifier":2}}
        # complexity is 10000
        # in the first turn you put input resources into object with action
        # then each turn you produce 100 base units multiplied by sum of each skills coefficient: if skill is lesser then min then you got the penalty, if its greater then min you will get bonus points (its counted below)
        # when you produce number of units equal to complexity, then you get output resources
        self.inputTypes = inputTypes
        self.outputTypes = outputTypes
        self.usedSkills = usedSkills
        self.complexity = complexity
        self.baseUnits = baseUnits
        self.interactableObject = interactableObject
        self.currentProgress = 0


    def process(self):
        self.currentProgress = self.currentProgress + self.baseUnits
        if self.currentProgress >= self.complexity:
            return {"completed": True, "output": self.outputTypes}
        else:
            return {"completed": False, "producedUnits": self.currentProgress}

    def doAction(self):
        # return self.process(input['producedUnits'])
        return self.process()