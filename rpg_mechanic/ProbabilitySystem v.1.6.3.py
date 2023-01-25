import os
import random
import tkinter as tk
from tkinter import ttk
from data_table import DataTable
from Weather import Weather
from WeatherGUI import WeatherGUI
from Actions import Actions
from Probability import Probability
from OutcomeWeights import OutcomeWeights
from OutcomeCustomizationTab import OutcomeCustomizationTab

class GameLogic:
    def __init__(self, weather, data_table, probability, outcome_weights):
        self.data_table = data_table
        self.weather = weather
        self.probability = probability
        self.outcome_weights = outcome_weights

    def perform_action(self, action):
        """
        Perform the given action, and return the outcome, success status, and true probability multiplier.
        :param action: The action to be performed.
        :return: Tuple of outcome, success status, and true probability multiplier.
        """
        probability = self.probability.get_probabilities().get(action)
        weather_modifier = self.weather.get_probabilities().get(action)
        true_prob_multiplier = probability * weather_modifier
        roll = random.randint(1, 16)
        outcome = self.data_table.table[roll]
        outcome_weight = self.outcome_weights.get_weight(outcome)
        true_prob_multiplier *= outcome_weight
        true_roll = roll * true_prob_multiplier
        success = true_roll > 8
        return (outcome, success, true_prob_multiplier)

class ButtonHandler:
    def __init__(self, tab, game_logic, display_outcome):
        # initialize the class variables game_logic, tab, and display_outcome
        self.game_logic = game_logic
        self.tab = tab
        self.display_outcome = display_outcome

        # create a button for each action in the probability object of game_logic
        for action in self.game_logic.probability.get_actions():
            # create a button with the text of the action
            button = tk.Button(self.tab, text=action, command=lambda action=action: self.display_outcome(self.game_logic.perform_action(action)))
            # pack the button to display it
            button.pack()
            # this loop iterates over the possible actions and creates a button for each one with the text of the action and a command to call the display_outcome function with the result of the perform_action function called on the action.
            # the buttons are then packed to display them on the tab.

class OutcomeHandler:
    def __init__(self, tab, game_logic):
        self.game_logic = game_logic
        self.tab = tab
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, action):
        outcome = action[0]
        success = action[1]
        probability = action[2]
        outcome_text = "Outcome: {} ({} with a probability of {})".format(outcome, "Success" if success else "Failure", probability)
        self.outcome_label.config(text=outcome_text)

import os
import tkinter as tk
from tkinter import ttk

class ProbabilityGUI:
    def __init__(self, tab, game_logic, actions, outcome_handler):
        self.tab = tab
        self.game_logic = game_logic
        self.actions = actions
        self.create_gui(outcome_handler)

    def create_gui(self, outcome_handler):
        button_frame = tk.Frame(self.tab)
        button_frame.pack()

        # Create the button to load the preset
        self.preset_var = tk.StringVar()
        self.preset_selector = ttk.OptionMenu(self.tab, self.preset_var, 'Default')
        self.populate_presets()
        self.preset_var.trace("w", self.load_preset)
        self.preset_selector.pack()

        # Create buttons for actions
        for action in self.actions.get_actions():
            button = tk.Button(button_frame, text=action, command=lambda action=action: outcome_handler.display_outcome(self.game_logic.perform_action(action)))
            button.pack(side=tk.LEFT)

    def populate_presets(self):
        preset_folder = "CustomPresets"
        preset_names = [f.split(".")[0] for f in os.listdir(preset_folder) if f.endswith(".txt")]
        self.preset_selector['menu'].delete(0, 'end')
        for preset in ['Default'] + preset_names:
            self.preset_selector['menu'].add_command(label=preset, command=lambda preset=preset: self.preset_var.set(preset))

    def load_preset(self, *args):
        selected_preset = self.preset_var.get()
        if selected_preset == "Default":
            self.game_logic.data_table.table = self.game_logic.data_table.default_outcomes.copy()
        else:
            preset_path = f"CustomPresets/{selected_preset}.txt"
            with open(preset_path, "r") as f:
                preset_outcomes = f.read().splitlines()
            self.game_logic.data_table.table = preset_outcomes

def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)

    # Create the player, enemy, weather, custom tabs
    player_tab = ttk.Frame(tab_control)
    enemy_tab = ttk.Frame(tab_control)
    weather_tab = ttk.Frame(tab_control)
    outcome_customization_tab = ttk.Frame(tab_control)

    # Create the classes
    actions = Actions()
    probability = Probability(actions.get_actions())
    outcome_weights = OutcomeWeights()
    data_table = DataTable(outcome_weights)

    weather = Weather()
    game_logic_player = GameLogic(weather, data_table, probability, outcome_weights)
    game_logic_enemy = GameLogic(weather, data_table, probability, outcome_weights)

    # Create the outcome handlers
    outcome_handler_player = OutcomeHandler(player_tab, game_logic_player)
    outcome_handler_enemy = OutcomeHandler(enemy_tab, game_logic_enemy)

    # Add the tabs to the tab control and pack it
    tab_control.add(player_tab, text="Player Tab")
    tab_control.add(enemy_tab, text="Enemy Tab")
    tab_control.add(weather_tab, text="Weather Tab")
    tab_control.add(outcome_customization_tab, text="Outcome Customization Tab")
    tab_control.pack()

    # Create the weather GUI
    weather_gui = WeatherGUI(weather, weather_tab)

    # Create the player and enemy GUI
    player_gui = ProbabilityGUI(player_tab, game_logic_player, actions, outcome_handler_player)
    enemy_gui = ProbabilityGUI(enemy_tab, game_logic_enemy, actions, outcome_handler_enemy)
    outcome_customization_gui = OutcomeCustomizationTab(outcome_customization_tab, data_table, outcome_weights, data_table.default_outcomes)

    # Create the preset selector dropdown menu
    preset_folder = 'CustomPresets'
    preset_names = [file for file in os.listdir(preset_folder) if file.endswith('.txt')]
    player_gui.preset_selector.pack()
    player_gui.preset_var.trace("w", lambda *args: player_gui.load_preset(player_gui.preset_var.get()))

    # Add this code after creating the player_gui object in the main method
    preset_folder = "CustomPresets"
    preset_names = [f.split(".")[0] for f in os.listdir(preset_folder) if os.path.isfile(os.path.join(preset_folder, f))]
    player_gui.preset_selector['menu'].delete(0, 'end')
    for preset in ['Default'] + preset_names:
        player_gui.preset_selector['menu'].add_command(label=preset, command=lambda preset=preset: player_gui.preset_var.set(preset))
    player_gui.load_preset(player_gui.preset_var.get())

    root.mainloop()

if __name__ == "__main__":
    main()
