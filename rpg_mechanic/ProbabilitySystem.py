import random
import tkinter as tk
from tkinter import ttk

class ProbabilitySystem:
    def __init__(self, tab, probabilities):
        self.probabilities = probabilities
        self.tab = tab
        self.create_gui()

    def create_gui(self):
        # Create buttons for the different actions
        for action in self.probabilities:
            button = tk.Button(self.tab, text=action.capitalize(), command=lambda action=action: self.display_outcome(action))
            button.pack()

        # Create a label to display the outcome
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def perform_action(self, action):
        probability = self.probabilities[action]
        roll = random.random()
        if roll <= probability:
            outcome = "success"
        else:
            outcome = "failure"
        return outcome

    def display_outcome(self, action):
        outcome = self.perform_action(action)
        self.outcome_label.config(text=f"Outcome: {outcome}")

def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)

    player_probabilities = {
        "attack": 0.8,
        "defend": 0.6,
        "cast spell": 0.9,
        "use skill": 0.7
    }
    player_tab = ttk.Frame(tab_control)
    tab_control.add(player_tab, text="Player")
    player_sys = ProbabilitySystem(player_tab, player_probabilities)

    enemies_probabilities = {
        "attack": 0.6,
        "defend": 0.8,
        "cast spell": 0.7,
        "use skill": 0.9
    }
    enemies_tab = ttk.Frame(tab_control)
    tab_control.add(enemies_tab, text="Enemies")
    enemies_sys = ProbabilitySystem(enemies_tab, enemies_probabilities)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()
