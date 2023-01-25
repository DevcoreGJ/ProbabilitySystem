import random
import tkinter as tk
from tkinter import ttk


class ProbabilityCalculator:
    def __init__(self, data_table, probabilities):
        self.data_table = data_table
        self.probabilities = probabilities

    def perform_action(self, action):
        roll = random.randint(1, 16)
        outcome_key = roll
        success = roll > 7
        outcome = self.data_table[outcome_key]
        return (outcome, success, outcome_key)

class GameLogic:
    def __init__(self, probabilities):
        self.data_table = DataTable()
        self.probability_calculator = ProbabilityCalculator(self.data_table, probabilities)

    def perform_action(self, action):
        outcome, success, outcome_key = self.probability_calculator.perform_action(action)
        return outcome, success, outcome_key

# This class creates the data table used for roll results
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

class ButtonHandler:
    def __init__(self, tab, game_logic, display_outcome):
        self.game_logic = game_logic
        self.tab = tab
        self.display_outcome = display_outcome

    def create_buttons(self):
        for action in self.game_logic.probabilities:
            button = tk.Button(self.tab, text=action.capitalize(), 
                               command=lambda action=action: self.display_outcome(self.probability_calculator.perform_action(action)))
            button.pack()

class OutcomeHandler:
    def __init__(self, tab):
        self.tab = tab
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, result):
        outcome, success = result
        outcome_text = "Outcome: {} ({})".format(outcome, "Success" if success else "Failure")
        self.outcome_label.config(text=outcome_text)

class ProbabilityGUI:
    def __init__(self, tab, probabilities):
        self.probabilities = probabilities
        self.tab = tab
        self.create_gui()
        
    def create_gui(self):
        self.outcome_handler = OutcomeHandler(self.tab)
        self.button_handler = ButtonHandler(self.tab, ProbabilityCalculator(DataTable(), self.probabilities), self.outcome_handler.display_outcome)
        self.button_handler.create_buttons()

def main():
    root = tk.Tk()
    root.title("Probability System")

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text="Tab 1")

    probability_gui = ProbabilityGUI(tab1, ["action1", "action2", "action3"])

    tab_control.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()
