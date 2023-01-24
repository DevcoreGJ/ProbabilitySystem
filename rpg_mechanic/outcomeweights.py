class OutcomeWeights:
    def __init__(self):
        self.weights = {
            "Critical Failure": 1,
            "Catastrophic Failure": 2,
            "Calamitous Failure": 4,
            "Distressing Failure": 32,
            "Rewarding Failure": 32,
            "Barely Success": 32,
            "Unrewarding Success": 16,
            "Rewarding Success": 16,
            "Comforting Success": 16,
            "Advantageous Success": 16,
            "Strategic Success": 16,
            "Prolific Success": 8,
            "Salvitic Success": 4,
            "Miraculous Success": 2,
            "Critical Success": 1,
        }

    def get_weight(self, outcome):
        return self.weights.get(outcome)

    def set_weight(self, outcome):
        if outcome in self.weights:
            return self.weights[outcome]
        else:
            raise ValueError(f'{outcome} is not a valid outcome')
