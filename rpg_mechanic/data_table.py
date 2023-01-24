class DataTable:
    def __init__(self, outcome_weights):
        self.table = {
            1: "Catastrophic Failure",
            2: "Calamitous Failure",
            3: "Distressing Failure",
            4: "Rewarding Failure",
            5: "Barely Success",
            6: "Unrewarding Success",
            7: "Rewarding Success",
            8: "Comforting Success",
            9: "Advantageous Success",
            10: "Strategic Success",
            11: "Prolific Success",
            12: "Salvitic Success",
            13: "Miraculous Success",
            14: "Critical Success",
            15: "Critical Failure",
            16: "Critical Success"
        }
        self.outcome_weights = outcome_weights
        self.default_table = self.table.copy() # Store a copy of the original table to use as the default
        self.default_outcomes = [outcome for outcome in self.table.values()] # Create a list of the default outcomes for easy reference





