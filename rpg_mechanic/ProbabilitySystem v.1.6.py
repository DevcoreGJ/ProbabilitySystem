import random
import tkinter as tk
from tkinter import ttk
from data_table import DataTable
from Weather import Weather
from Probability import Probability

class ProbabilitySystem:
    def __init__(self, data_table, weather, probabilities):
        self.data_table = data_table
        self.weather = weather
        self.probability = Probability(probabilities)

    def perform_action(self, action):
        probability = self.probability.probabilities[action]
        roll = random.randint(1, 16)
        success = roll > 7
        outcome = self.data_table.table[roll]
        return (outcome, success, probability)


class GameLogic:
    def __init__(self, weather, data_table):
        self.data_table = data_table
        self.weather = weather
        probability = Probability(weather.get_probabilities())
        self.probability_system = ProbabilitySystem(data_table, weather, probability)

    def perform_action(self, action):
        return self.probability_system.perform_action(action)

class ButtonHandler:
    def __init__(self, tab, game_logic, display_outcome):
        self.game_logic = game_logic
        self.tab = tab
        self.display_outcome = display_outcome

    def create_buttons(self):
            for action in self.game_logic.weather.get_probabilities():
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

    def display_outcome(self, action):
        outcome, success = self.game_logic.perform_action(action)
        probability = self.game_logic.weather.get_probabilities()[action]
        outcome_text = "Outcome: {} ({} with a probability of {})".format(outcome, "Success" if success else "Failure", probability)
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
        self.weather_var = tk.StringVar(value=self.probability_system.weather.current_condition)
        self.weather_selector = ttk.Combobox(self.tab, textvariable=self.weather_var, values=list(self.probability_system.weather.conditions.keys()))
        self.weather_selector.pack()
        self.weather_selector.bind("<<ComboboxSelected>>", self.update_weather)

    def update_weather(self, event):
        self.probability_system.weather.set_weather(self.weather_var.get())
        self.probability_system.probability.probabilities = self.probability_system.weather.get_probabilities()
        self.button_handler.create_buttons()

def main():
    root = tk.Tk()
    root.title("Probability System")
    tab_control = ttk.Notebook(root)
    data_table = DataTable()
    weather = Weather()
    probabilities = {"attack": 0.8, "defend": 0.6, "cast spell": 0.9, "use skill": 0.7, "heal": 0.4,}
    game_logic = GameLogic(weather, data_table)
    tab = ttk.Frame(tab_control)
    probability_gui = ProbabilityGUI(tab, game_logic)

    # Create the player and enemy tabs
    player_tab = ttk.Frame(tab_control)
    enemy_tab = ttk.Frame(tab_control)
    weather_tab = ttk.Frame(tab_control)

    player_sys = ProbabilityGUI(player_tab, game_logic)
    enemy_sys = ProbabilityGUI(enemy_tab, game_logic)
    weather_sys = ProbabilityGUI(weather_tab, game_logic)

    tab_control.add(player_tab, text="Player Tab")
    tab_control.add(enemy_tab, text="Enemy Tab")
    tab_control.add(weather_tab, text="Weather Tab")
    tab_control.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
