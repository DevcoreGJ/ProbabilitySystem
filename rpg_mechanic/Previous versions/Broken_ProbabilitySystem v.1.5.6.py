import random
import tkinter as tk
from tkinter import ttk

    # This class handles the probability calculations and roll results
"""
    The ProbabilityLogic class contains the logic for determining the outcome of an action based on a set of probabilities
    and a data table.
"""
class ProbabilityCalculator:
    def __init__(self, data_table, probabilities):
        self.data_table = data_table
        self.probabilities = probabilities

    def perform_action(self, action):
        probability = self.probabilities[action]
        roll = random.randint(1, 16) # added this line
        success = roll > 7
        outcome = self.data_table.table[roll]
        return (outcome, success)

class GameLogic:
    def __init__(self, probabilities, data_table):
        self.data_table = data_table # change here
        self.ProbabilityCalculator = ProbabilityCalculator(data_table, probabilities)
        self.probabilities = probabilities # new line

    def perform_action(self, action):
        outcome, success = self.ProbabilityCalculator.perform_action(action)
        return (outcome, success)

'''
data_table = DataTable()
probability_logic = ProbabilityLogic(data_table)
success, outcome = probability_logic.perform_action()
print(success, outcome)
'''

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
            button = tk.Button(self.tab, text=action,
                                command=lambda action=action:
    self.display_outcome(self.game_logic.perform_action(action)))
            button.pack()

class OutcomeHandler:
    def __init__(self, tab, game_logic):
        self.game_logic = game_logic
        self.tab = tab
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, result):
        outcome, success = self.game_logic.perform_action(result) # accessing game_logic here
        outcome_text = "Outcome: {} ({})".format(outcome, "Success" if success else "Failure")
        self.outcome_label.config(text=outcome_text)
    
class ProbabilityGUI: # changed this line:
    def __init__(self, tab, game_logic):
        self.game_logic = game_logic
        self.tab = tab
        self.create_gui()

    def create_gui(self):
        self.outcome_handler = OutcomeHandler(self.tab, self.game_logic) # passing game_logic here
        self.button_handler = ButtonHandler(self.tab, self.game_logic, self.outcome_handler.display_outcome)
        self.button_handler.create_buttons()

def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)
    data_table = DataTable()
    probabilities = {"attack": 0.8, "defend": 0.6, "cast spell": 0.9, "use skill": 0.7, "heal": 0.4,}
    game_logic = GameLogic(probabilities, data_table)
    tab = ttk.Frame(root)

    probability_gui = ProbabilityGUI(tab, game_logic) # changed this line
    probability_gui.create_gui()
    player_logic = GameLogic(DataTable(), probabilities)
    enemy_logic = ProbabilityCalculator(DataTable(), probabilities)
    # Create the player and enemy tabs
    player_tab = ttk.Frame(tab_control)
    enemy_tab = ttk.Frame(tab_control)
    tab.pack() # added this line
    # Add the player and enemy tabs to the tab control

    tab_control.add(player_tab, text='Player')
    tab_control.add(enemy_tab, text='Enemy')
    tab_control.pack(expand=1, fill='both')

    player_sys = ProbabilityGUI(player_tab, probabilities)
    enemy_sys = ProbabilityGUI(enemy_tab, probabilities)
    root.mainloop()

if __name__ == "__main__":
    main()
