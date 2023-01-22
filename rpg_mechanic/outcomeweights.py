class OutcomeWeights:
    def __init__(self):
        self.weights = {
            "Critical Failure": 1,
            "Catastrophic Failure": 2,
            "Calamitous Failure": 4,
            "Distressing Failure": 8,
            "Rewarding Failure": 16,
            "Barely Success": 16,
            "Unrewarding Success": 32,
            "Rewarding Success": 32,
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
