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
        probabilities = self.probabilities[action]
        roll = random.randint(1, 44)
        success = roll > 16
        outcome = self.data_table.table[roll]
        return (outcome, success)

class GameLogic:
    def __init__(self, probabilities):
        self.data_table = DataTable()
        self.ProbabilityCalculator = ProbabilityCalculator(self.data_table.table[roll], probabilities)

    def perform_action(self, action):
        outcome, success = self.probability_calculator.perform_action(action)
        return outcome, success


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
            3: "Apocalyptic Failure",
            4: "Apocalyptic Failure",
            5: "Catastrophic Failure",
            6: "Catastrophic Failure",
            7: "Catastrophic Failure",
            8: "Calamitous Failure",
            9: "Calamitous Failure",
            10: "Calamitous Failure",
            11: "Distressing Failure",
            12: "Distressing Failure",
            13: "Distressing Failure",
            14: "Rewarding Failure",
            15: "Rewarding Failure",
            16: "Rewarding Failure",
            17: "Barely Success",
            18: "Barely Success",
            19: "Barely Success",
            20: "Unrewarding Success",
            21: "Unrewarding Success",
            22: "Unrewarding Success",
            23: "Rewarding Success",
            24: "Rewarding Success",
            25: "Rewarding Success",
            26: "Comforting Success",
            27: "Comforting Success",
            28: "Comforting Success",
            29: "Advantageous Success",
            30: "Advantageous Success",
            31: "Advantageous Success",
            32: "Strategic Success",
            33: "Strategic Success",
            34: "Strategic Success",
            35: "Prolific Success",
            36: "Prolific Success",
            37: "Prolific Success",
            38: "Salvitic Success",
            39: "Salvitic Success",
            40: "Salvitic Success",
            41: "Miraculous Success",
            42: "Miraculous Success",
            43: "Miraculous Success",
            44: "Critical Success"
}

class ButtonHandler:
    def __init__(self, tab, ProbabilityCalculator, display_outcome):
        self.ProbabilityCalculator = ProbabilityCalculator
        self.tab = tab
        self.display_outcome = display_outcome

    def create_buttons(self):
        for action in self.ProbabilityCalculator.probabilities:
            button = tk.Button(self.tab, text=action.capitalize(), 
                               command=lambda action=action: self.display_outcome(self.ProbabilityCalculator.perform_action(action),))
            button.pack()



class OutcomeHandler:
    def __init__(self, tab, probabilities):
        self.probabilities = probabilities
        self.tab = tab
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, result):
        outcome, success = result
        outcome_text = "Outcome: {} ({})".format(outcome, "Success" if success else "Failure")
        self.outcome_label.config(text=outcome)
        self.outcome_label.config(text=outcome_text)

class ProbabilityGUI:
    def __init__(self, tab, probabilities):
        self.probabilities = probabilities
        self.tab = tab
        self.create_gui()
        
    def create_gui(self):
        self.outcome_handler = OutcomeHandler(self.tab, self.probabilities)
        self.button_handler = ButtonHandler(self.tab, self.probabilities, self.outcome_handler.display_outcome)
        self.button_handler.create_buttons()
    

def main():
    """
main()
This is the main function of the program that creates the GUI and sets up the different probability systems.
It starts by creating the root window using tkinter's Tk() class, setting its title to "Probability System",
and creating a tab control using ttk's Notebook() class.
Next, it sets up the player and enemy probability systems by creating a dictionary of probabilities for each action,
creating a tab for each system in the tab control, creating a ProbabilityLogic instance for each system,
passing in the dictionary of probabilities and a DataTable() instance, and creating a ProbabilityGUI instance for each system,
passing in the corresponding tab and ProbabilityLogic instance.
Finally, it packs the tab control to fill the entire window and starts the main loop to keep the window running.
"""
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)
    player_probabilities = {"attack": 0.8, "defend": 0.6, "cast spell": 0.9, "use skill": 0.7, "heal": 0.4}
    #player_tab = ttk.Frame(tab_control)
    #tab_control.add(player_tab, text="Player")
    player_logic = ProbabilityCalculator(DataTable(), player_probabilities)
    #player_sys = ProbabilityGUI(player_tab, player_logic)

    # Create the player and enemy tabs
    player_tab = ttk.Frame(tab_control)
    enemies_tab = ttk.Frame(tab_control)

    # Add the player and enemy tabs to the tab control
    tab_control.add(player_tab, text='Player')
    tab_control.add(enemies_tab, text='Enemy')
    tab_control.pack(expand=1, fill='both')

    enemies_probabilities = {"attack": 0.6, "defend": 0.4,"cast spell": 0.9, "use skill": 0.7, "heal": 0.2}
    #enemies_tab = ttk.Frame(tab_control)
    #tab_control.add(enemies_tab, text="Enemies")
    enemies_logic = ProbabilityCalculator(DataTable(), enemies_probabilities)
    #enemies_sys = ProbabilityGUI(enemies_tab, enemies_logic)

    player_sys = ProbabilityGUI(player_tab, player_logic)
    enemies_sys = ProbabilityGUI(enemies_tab, enemies_logic)

    #tab_control.pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    main()
