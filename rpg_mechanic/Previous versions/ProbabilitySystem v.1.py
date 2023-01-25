import random
import tkinter as tk

class ProbabilitySystem:
    def __init__(self):
        self.probabilities = {
            "attack": 0.8,
            "defend": 0.6,
            "cast spell": 0.9,
            "use skill": 0.7
        }
        self.root = tk.Tk()
        self.root.title("Chart-based Probability System")
        self.create_gui()

    def create_gui(self):
        # Create buttons for the different actions
        self.attack_button = tk.Button(self.root, text="Attack", command=lambda: self.display_outcome("attack"))
        self.attack_button.pack()
        self.defend_button = tk.Button(self.root, text="Defend", command=lambda: self.display_outcome("defend"))
        self.defend_button.pack()
        self.spell_button = tk.Button(self.root, text="Cast Spell", command=lambda: self.display_outcome("cast spell"))
        self.spell_button.pack()
        self.skill_button = tk.Button(self.root, text="Use Skill", command=lambda: self.display_outcome("use skill"))
        self.skill_button.pack()

        # Create a label to display the outcome
        self.outcome_label = tk.Label(self.root)
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

    def run(self):
        self.root.mainloop()

prob_sys = ProbabilitySystem()
prob_sys.run()

''' 
This version of the code creates a ProbabilitySystem class that holds the probabilities table, GUI elements and the functions that handle the actions and display the outcome.
The class has a constructor __init__ that initializes the class properties, creates the GUI and runs the mainloop.
It also split the functions create_gui, perform_action, display_outcome and run to make the code more readable and maintainable.

This is still a simple example and you can add more complexity to the system as desired. This version of the code makes it easy to add new methods, properties or even inherit from it. 
'''
