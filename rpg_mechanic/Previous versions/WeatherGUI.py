import random
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import OptionMenu
from Weather import Weather

class WeatherGUI:
	def __init__(self, weather, weather_tab):
		self.weather = weather
		self.weather_tab = weather_tab
		self.create_gui()

	def create_gui(self):
		self.weather_var = tk.StringVar(value=self.weather.current_condition)
		self.weather_selector = ttk.Combobox(self.weather_tab, textvariable=self.weather_var, values=list(self.weather.conditions.keys()))
		self.weather_selector.bind("<<ComboboxSelected>>", self.update_weather)

		self.weather_selector.pack()

	
	def update_weather(self, event):
		self.weather.set_weather(self.weather_var.get())
