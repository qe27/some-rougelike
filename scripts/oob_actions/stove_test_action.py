from scripts.process_action import ProcessAction


# class for test purposes
class StoveTestAction(ProcessAction):

    def __init__(self, interactableObject):
        ProcessAction.__init__(self, interactableObject, outputTypes={"food": 1}, complexity=200)
