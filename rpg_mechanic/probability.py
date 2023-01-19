class Probability:
    def __init__(self, probabilities):
        self.probabilities = probabilities

    def get_probability(self, action):
        return self.probabilities.get(action, None)
        
