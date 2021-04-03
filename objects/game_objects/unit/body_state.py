class ManipulationLimb:

    def __init__(self, name, fingers):
        # model of limbs
        self.name = name
        # self.maxSuckers = maxSuckers
        # self.suckers = suckers
        # self.maxFingers = maxFingers
        self.fingers = fingers


class BodyState:

    def __init__(self, manipulationLimbs):
        self.manipulationLimbs = manipulationLimbs
