import random
import tkinter as tk
from tkinter import ttk
from data_table import DataTable
from Weather import Weather
from WeatherGUI import WeatherGUI
from Probability import Probability

class ProbabilitySystem:
    def __init__(self, data_table, weather, probability):
        self.data_table = data_table
        self.weather = weather
        self.probability = probability

    def perform_action(self, action):
        probability = self.probability.get_probability(action)
        roll = random.randint(1, 16)
        success = roll > 7
        outcome = self.data_table.table[roll]
        return (outcome, success, probability)

class GameLogic:
    def __init__(self, weather, data_table):
        self.data_table = data_table
        self.weather = weather
        self.probability = Probability(weather.get_probabilities())
        self.probability_system = ProbabilitySystem(data_table, weather, self.probability)

    def perform_action(self, action):
        return self.probability_system.perform_action(action)

class ButtonHandler:
    def __init__(self, tab, game_logic, display_outcome):
        self.game_logic = game_logic
        self.tab = tab
        self.display_outcome = display_outcome

    def create_buttons(self):
        for action in self.game_logic.weather.get_probabilities():
            button = tk.Button(self.tab, text=action, command=lambda action=action: self.display_outcome(self.game_logic.perform_action(action)))
            button.pack()

class OutcomeHandler:
    def __init__(self, tab, game_logic):
        self.game_logic = game_logic
        self.tab = tab
        self.outcome_label = tk.Label(self.tab)
        self.outcome_label.pack()

    def display_outcome(self, action):
        outcome, success, actual_probability = self.game_logic.perform_action(action)
        outcome_text = "Outcome: {} ({} with a probability of {})".format(outcome, "Success" if success else "Failure", actual_probability)
        self.outcome_label.config(text=outcome_text)


class ProbabilityGUI:
    def __init__(self, tab, probability_system):
        self.probability_system = probability_system
        self.tab = tab
        self.create_gui()

    def create_gui(self):
        self.outcome_handler = OutcomeHandler(self.tab, self.probability_system)
        self.button_handler = ButtonHandler(self.tab, self.probability_system, self.outcome_handler.display_outcome)
        self.button_handler.create_buttons()

def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)
    probabilities = {"attack": 0.8, "defend": 0.6, "cast spell": 0.9, "use skill": 0.7, "heal": 0.4}
    probability = Probability(probabilities)
    
    data_table = DataTable()
    
    tab = ttk.Frame(tab_control)


    # Create the player and enemy tabs
    player_tab = ttk.Frame(tab_control)
    enemy_tab = ttk.Frame(tab_control)
    weather_tab = ttk.Frame(tab_control)
    
    

    tab_control.add(player_tab, text="Player Tab")
    tab_control.add(enemy_tab, text="Enemy Tab")
    tab_control.add(weather_tab, text="Weather Tab")
    tab_control.pack()
    weather = Weather()
    game_logic = GameLogic(weather, data_table)
    probability_gui = ProbabilityGUI(tab, game_logic)
    weather_gui = WeatherGUI(weather, weather_tab)
    player_sys = ProbabilityGUI(player_tab, game_logic)
    enemy_sys = ProbabilityGUI(enemy_tab, game_logic)
    root.mainloop()


if __name__ == "__main__":
    main()
