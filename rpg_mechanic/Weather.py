import random
import tkinter as tk
from tkinter import ttk

class Weather:
    def __init__(self):
        self.conditions = {
            "sunny": {"attack": 0.8, "defend": 0.6, "cast spell": 0.9, "use skill": 0.7, "heal": 0.4},
            "rainy": {"attack": 0.7, "defend": 0.7, "cast spell": 0.8, "use skill": 0.6, "heal": 0.5},
            "snowy": {"attack": 0.6, "defend": 0.8, "cast spell": 0.7, "use skill": 0.5, "heal": 0.6},
        }
        self.current_condition = "sunny"

    def set_weather(self, condition):
        if condition in self.conditions:
            self.current_condition = condition
        else:
            print(f"Invalid weather condition: {condition}")

    def get_probabilities(self):
        return self.conditions[self.current_condition]

