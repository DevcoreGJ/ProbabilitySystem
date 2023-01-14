import random
from tkinter import ttk
import tkinter as tk

class ProbabilitySystem:
    def __init__(self, tab):
        self.probabilities = {
            "attack": 0.8,
            "defend": 0.6,
            "cast spell": 0.9,
            "use skill": 0.7
        }
        self.tab = tab
        self.create_gui()

    def create_gui(self):
        # Create buttons for the different actions
        self.attack_button = tk.Button(self.tab, text="Attack", command=lambda: self.display_outcome("attack"))
        self.attack_button.pack()
        self.defend_button = tk.Button(self.tab, text="Defend", command=lambda: self.display_outcome("defend"))
        self.defend_button.pack()
        self.spell_button = tk.Button(self.tab, text="Cast Spell", command=lambda: self.display_outcome("cast spell"))
        self.spell_button.pack()
        self.skill_button = tk.Button(self.tab, text="Use Skill", command=lambda: self.display_outcome("use skill"))
        self.skill_button.pack()

        # Create a label to display the outcome
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, action):
        probability = self.probabilities[action]
        roll = random.random()
        if roll <= probability:
            outcome = "success"
        else:
            outcome = "failure"
        self.outcome_label.config(text=f"Outcome: {outcome}")

def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)

    player_tab = ttk.Frame(tab_control)
    tab_control.add(player_tab, text="Player")
    prob_sys = ProbabilitySystem(player_tab)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()
