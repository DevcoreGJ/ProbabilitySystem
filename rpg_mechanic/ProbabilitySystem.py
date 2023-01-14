import random
import tkinter as tk
from tkinter import ttk

    # This class handles the probability calculations and roll results
"""
    The ProbabilityLogic class contains the logic for determining the outcome of an action based on a set of probabilities
    and a data table.
"""
class ProbabilityLogic:
    def __init__(self, probabilities, data_table):
        """
        Initialize the ProbabilityLogic class with the set of probabilities and data table.
        :param probabilities: A dictionary of actions and their corresponding probabilities of success.
        :param data_table: A list of possible outcomes for a roll, with "Critical Failure" at index 0,
                           "Failure x" or "Success x" at indices 1 to 43, and "Critical Success" at index 44.
        """
        self.probabilities = probabilities
        self.data_table = data_table

    def perform_action(self, action):
        """
            Perform the specified action and determine the outcome based on the probability and data table.
            
            :param action: The action to perform.
            :return: A tuple containing a boolean indicating success or failure, and the outcome from the data table.
        """
        # Get the probability of success for the selected action
        probability = self.probabilities[action]
        # Roll a random number between 1 and 44
        roll = random.randint(1, 44)
        # Get the outcome from the data table using the roll result as the index
        outcome = self.data_table.table[roll-1]
        # Determine if the outcome is a success or failure
        success = outcome[:7] == "Success"
        return success, outcome


# This class creates the data table used for roll results
class DataTable:
    """
    The DataTable class contains a list of possible outcomes for a roll.

    """
    def __init__(self):
        """
        Initialize the DataTable class with a list of possible outcomes.
        """
        # Create a list of outcomes with the first element as "Critical Failure", 
        # the next 42 elements as "Failure x" or "Success x" based on their index, 
        # and the last element as "Critical Success"
        self.table = ["Critical Failure"] + [f"{'Failure' if i < 16 else 'Success'} {i}" for i in range(2, 44)] + ["Critical Success"]


# This class handles the GUI and displaying of results
class ProbabilityGUI:
    """
    The ProbabilityGUI class contains the graphical user interface for the probability system.
    """
    def __init__(self, tab, probability_logic):
        self.probability_logic = probability_logic
        self.tab = tab
        self.create_gui()

    def create_gui(self):
        # Create buttons for the different actions
        for action in self.probability_logic.probabilities:
            button = tk.Button(self.tab, text=action.capitalize(), command=lambda action=action: self.display_outcome(action))
            button.pack()

        # Create a label to display the outcome
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, action):
        # Get the success and outcome from the probability logic class
        success, outcome = self.probability_logic.perform_action(action)
        # Update the outcome label with the outcome and success/failure status
        self.outcome_label.config(text=f"Outcome: {outcome} ({'Success' if success else 'Failure'})")

        
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

    player_probabilities = {
    "attack": 0.8,
    "defend": 0.6,
    "cast spell": 0.9,
    "use skill": 0.7
    }
    player_tab = ttk.Frame(tab_control)
    tab_control.add(player_tab, text="Player")
    player_logic = ProbabilityLogic(player_probabilities, DataTable())
    player_sys = ProbabilityGUI(player_tab, player_logic)

    enemies_probabilities = {
    "attack": 0.6,
    "defend": 0.8,
    "cast spell": 0.7,
    "use skill": 0.9
    }
    enemies_tab = ttk.Frame(tab_control)
    tab_control.add(enemies_tab, text="Enemies")
    enemies_logic = ProbabilityLogic(enemies_probabilities, DataTable())
    enemies_sys = ProbabilityGUI(enemies_tab, enemies_logic)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()


if __name__ == "__main__":
    main()
