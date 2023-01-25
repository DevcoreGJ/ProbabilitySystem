Probability System v.1.5.8
This version of the probability system includes several updates to the design and implementation of the code. The main changes include:
A new class called Probability has been added to separate the probability calculations from the rest of the code.
The GameLogic class has been updated to use the new Probability class and the updated ProbabilityCalculator class.
The ButtonHandler class has been updated to reference the new variable name for the probability class (self.probability) instead of the old variable name (self.probabilities)
The OutcomeHandler class has been updated to reflect the new data structure of the returned value from the GameLogic class's perform_action method.
The game_logic variable in the main function has been updated to reflect the new class structure.
To use this version of the probability system, simply run the program in a python environment and click the buttons to see the outcome and success of each action.
Please note that this version of the probability system is still a work in progress and there may be additional updates and changes in future versions.

