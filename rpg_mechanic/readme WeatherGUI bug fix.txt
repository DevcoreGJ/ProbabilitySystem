Weather Tab Fix

A bug was identified in the WeatherGUI class where the weather_var variable was not defined properly.
The variable was defined within the create_gui method but was not referenced as self.weather_var when being passed as an argument to the ttk.Combobox constructor.

The solution was to add the self keyword to the variable definition so that it would be accessible throughout the class as self.weather_var. 
This allows the variable to be referenced properly in the update_weather method.