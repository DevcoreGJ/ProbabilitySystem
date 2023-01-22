import random
import tkinter as tk
from tkinter import ttk

class Weather:
    def __init__(self):
        self.conditions = {
            "clear": {"attack": 1, "defend": 1, "cast spell": 1, "use skill": 1, "heal": 1},
            "sunny": {"attack": 1, "defend": 0.9, "cast spell": 1.1, "use skill": 1, "heal": 0.8},
            "rainy": {"attack": 0.9, "defend": 1.1, "cast spell": 0.9, "use skill": 0.9, "heal": 1},
            "snowy": {"attack": 0.8, "defend": 1.2, "cast spell": 0.8, "use skill": 0.8, "heal": 1.1},
        }
        self.current_condition = "clear"

    def set_weather(self, condition):
        if condition in self.conditions:
            self.current_condition = condition
        else:
            print(f"Invalid weather condition: {condition}")

    def get_probabilities(self):
        return self.conditions[self.current_condition]
