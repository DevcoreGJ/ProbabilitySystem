import random
import tkinter as tk
from tkinter import ttk
from data_table import DataTable
from Weather import Weather
from WeatherGUI import WeatherGUI
from Actions import Actions
from Probability import Probability

class GameLogic:
    def __init__(self, weather, data_table, probability):
        self.data_table = data_table
        self.weather = weather
        self.probability = probability

    def perform_action(self, action):
        probability = self.probability.get_probabilities().get(action)
        weather_modifier = self.weather.get_probabilities().get(action)
        true_prob_multiplier = probability * weather_modifier
        roll = random.randint(1, 16)
        true_roll = roll * true_prob_multiplier
        success = true_roll > 8
        outcome = self.data_table.table[roll]
        return (outcome, success, true_prob_multiplier)

class ButtonHandler:
    def __init__(self, tab, game_logic, display_outcome):
        self.game_logic = game_logic
        self.tab = tab
        self.display_outcome = display_outcome

        for action in self.game_logic.probability.get_actions():
            button = tk.Button(self.tab, text=action, command=lambda action=action: self.display_outcome(self.game_logic.perform_action(action)))
            button.pack()


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

class ProbabilityGUI:
    def __init__(self, tab, game_logic, actions, outcome_handler):
        self.tab = tab
        self.game_logic = game_logic
        self.actions = actions
        self.create_gui(outcome_handler)

    def create_gui(self, outcome_handler):
        for action in self.actions.get_actions():
            button = tk.Button(self.tab, text=action, command=lambda action=action: outcome_handler.display_outcome(self.game_logic.perform_action(action)))
            button.pack()
def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)

    # Create the player, enemy and weather tabs
    player_tab = ttk.Frame(tab_control)
    enemy_tab = ttk.Frame(tab_control)
    weather_tab = ttk.Frame(tab_control)

    # Create the classes
    actions = Actions()
    probability = Probability(actions.get_actions())
    data_table = DataTable()
    weather = Weather()
    game_logic_player = GameLogic(weather, data_table, probability)
    game_logic_enemy = GameLogic(weather, data_table, probability)
    
    # Create the outcome handlers
    outcome_handler_player = OutcomeHandler(player_tab, game_logic_player)
    outcome_handler_enemy = OutcomeHandler(enemy_tab, game_logic_enemy)

    # Add the tabs to the tab control and pack it
    tab_control.add(player_tab, text="Player Tab")
    tab_control.add(enemy_tab, text="Enemy Tab")
    tab_control.add(weather_tab, text="Weather Tab")
    tab_control.pack()

    # Create the weather GUI
    weather_gui = WeatherGUI(weather, weather_tab)

    # Create the player and enemy GUI
    player_gui = ProbabilityGUI(player_tab, game_logic_player, actions, outcome_handler_player)
    enemy_gui = ProbabilityGUI(enemy_tab, game_logic_enemy, actions, outcome_handler_enemy)
    root.mainloop()

if __name__ == "__main__":
    main()
