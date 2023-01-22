class Probability:
    def __init__(self, actions):
        self.actions = actions
        self.probabilities = {}
        for action in actions:
            self.probabilities[action] = 1.0

    def get_probabilities(self):
        return self.probabilities

    def get_actions(self):
        return self.actions
