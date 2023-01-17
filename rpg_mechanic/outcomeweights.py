import random

class OutcomeWeights:
    def __init__(self, outcomes):
        self.outcomes = outcomes
        self.total_weight = sum(outcomes.values())
        
    def normalize_weights(self):
        """
        normalize the weights by dividing each weight by the total weight
        """
        total_weight = sum(self.outcomes.values())
        for outcome, weight in self.outcomes.items():
            self.outcomes[outcome] = weight / total_weight
        
    def get_cumulative_probabilities(self):
        """
        create a dictionary of cumulative probabilities for each outcome
        """
        cumulative_probability = 0
        cumulative_probabilities = {}
        for outcome, weight in self.outcomes.items():
            cumulative_probability += weight
            cumulative_probabilities[outcome] = cumulative_probability
        return cumulative_probabilities

    def get_outcome(self, roll):
        """
        get the outcome corresponding to a given roll
        """
        cumulative_probabilities = self.get_cumulative_probabilities()
        for outcome, cumulative_probability in cumulative_probabilities.items():
            if roll <= cumulative_probability:
                return outcome
                
    def get_weight_percentage(self, outcome):
        outcome_weight = self.outcomes[outcome]
        return outcome_weight / self.total_weight * 100

    def roll_outcome(self):
        """
        roll for an outcome and return it
        """
        roll = random.random()
        for outcome in self.outcomes:
            print(f"{outcome}: {self.get_weight_percentage(outcome)}%")
        outcome =  self.get_outcome(roll)
        print(f'Rolled Outcome: {outcome}')
        return outcome

def main():
    outcomes = {
        "Catastrophic Failure": 4,
        "Calamitous Failure": 5,
        "Distressing Failure": 6,
        "Rewarding Failure": 7,
        "Barely Success": 8,
        "Unrewarding Success": 9,
        "Rewarding Success": 10,
        "Comforting Success": 9,
        "Advantageous Success": 8,
        "Strategic Success": 7,
        "Prolific Success": 6,
        "Salvitic Success": 5,
        "Miraculous Success": 4,
        "Critical Success": 2,
        "Critical Failure": 2
}

    weights = OutcomeWeights(outcomes)
    weights.normalize_weights()
    outcome = weights.roll_outcome()

if __name__ == "__main__":
    main()
