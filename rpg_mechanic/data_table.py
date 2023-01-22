import random
import tkinter as tk
from tkinter import ttk

class Probability:
    def __init__(self, probability):
        self.probabilities = probabilities

    def perform_action(self, probabilities):
        probability = self.probabilities[action]
        roll = random.randint(1, 16)
        success = roll > 7
        return (roll, success)

class DataTable:
    def __init__(self):
        self.table = {
            1: "Critical Failure",
            2: "Apocalyptic Failure",
            3: "Catastrophic Failure",
            4: "Calamitous Failure",
            5: "Distressing Failure",
            6: "Rewarding Failure",
            7: "Barely Success",
            8: "Unrewarding Success",
            9: "Rewarding Success",
            10: "Comforting Success",
            11: "Advantageous Success",
            12: "Strategic Success",
            13: "Prolific Success",
            14: "Salvitic Success",
            15: "Miraculous Success",
            16: "Critical Success"
        }

class ProbabilityCalculator:
    def __init__(self, data_table, probability):
        self.data_table = data_


