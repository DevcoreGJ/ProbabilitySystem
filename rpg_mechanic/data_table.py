import random
import tkinter as tk
from tkinter import ttk

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

    def get_outcome(self, roll):
        return self.table[roll]

    def get_outcome_weight(self, outcome):
        return self.outcome_weights.get(outcome, 1)



