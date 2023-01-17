import random
import tkinter as tk
from tkinter import ttk

class Probability:
    def __init__(self, probabilities):
        self.probabilities = probabilities

    def perform_action(self, action):
        probability = self.probabilities[action]
        roll = random.randint(1, 16)
        success = roll > 7
        return (roll, success)


class ProbabilityCalculator:
    def __init__(self, data_table, probability):
        self.data_table = data_table
        self.probability = probability

    def perform_action(self, action):
        roll, success = self.probability.perform_action(action)
        outcome = self.data_table.table[roll]
        return (outcome, success)


class GameLogic:
    def __init__(self, probabilities, data_table):
        self.data_table = data_table
        self.probability = Probability(probabilities)
        self.probability_calculator = ProbabilityCalculator(data_table, self.probability)

    def perform_action(self, action):
        return self.probability_calculator.perform_action(action)
        return (outcome, success)

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
        for action in self.game_logic.probability.probabilities:
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
        outcome, success = result
        outcome_text = "Outcome: {} ({})".format(outcome, "Success" if success else "Failure")
        self.outcome_label.config(text=outcome_text)

class ProbabilityGUI:
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
    tab = ttk.Frame(tab_control)
    probability_gui = ProbabilityGUI(tab, game_logic)
    
    # Create the player and enemy tabs
    player_tab = ttk.Frame(tab_control)
    enemy_tab = ttk.Frame(tab_control)

    player_sys = ProbabilityGUI(player_tab, game_logic)
    enemy_sys = ProbabilityGUI(enemy_tab, game_logic)

    tab_control.add(player_tab, text="Player Tab")
    tab_control.add(enemy_tab, text="Enemy Tab")
    tab_control.pack()
    root.mainloop()


if __name__ == "__main__":
    main()