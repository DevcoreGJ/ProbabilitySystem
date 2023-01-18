class Probability:
    def __init__(self, probabilities):
        self.probabilities = probabilities

    def perform_action(self, action):
        probability = self.probabilities[action]
        roll = random.randint(1, 16)
        success = roll > 7
        outcome = self.data_table.table[roll]
        return (outcome, success, probability)