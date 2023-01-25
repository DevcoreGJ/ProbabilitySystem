Overview

This is a probability system for a role-playing game. The system includes a game logic class that uses a probability calculator and data table to determine the outcome of actions in the game. The system also includes a graphical user interface (GUI) that allows players to select actions and view the outcomes.
Future Work

    Making additional tabs including but not limited to:
        Weather: to simulate the effect of weather on the game
        Front End for users to alter the results for DataTable outcomes: this will allow users to customize the outcome of the game.
        Front End for users to alter actions: this will allow users to add or remove actions in the game.
    Create a separate class for the probabilities, which can handle the probability calculations and outcome determination. This will separate the probability logic from the data table logic.
    Create a separate class for the data table, which can handle the creation and storage of the data table. This will separate the data table logic from the probability logic.
    Use object-oriented principles, such as inheritance and polymorphism, to create a more flexible and extensible codebase.
    Create a config file to store the data table and probabilities, which could be easily modified without the need to change the code.
    Use a logging module for better debugging, which will print all the logs to a file for later analysis.
    Break down the main function into smaller functions, this will make it more readable and easy to understand.
    Add comments throughout the code, explaining the purpose and functionality of each class, method, and variable.

Considerations

    The system currently uses a fixed data table and set of probabilities, but in the future, it could be expanded to allow for user customization.
    The GUI is currently basic and could be expanded to include more features and a more polished design.
    The system currently only supports a single player, but it could be expanded to support multiple players in the future.

Timeline

    2 weeks: Create the separate classes for probabilities and data table and implement object-oriented principles. Done
    2 weeks: Create the config file and implement logging. Next.
    2 weeks: Break down the main function and add comments. Ongoing.
    2 weeks: Implement additional tabs and front-end features Doing.
    2 weeks: Testing and debugging. Ongoing.
    2 weeks: Finalizing and polishing the GUI design. Neverending.

Introduction

This is a probability system that simulates the outcome of different actions in a role-playing game. It uses a GUI built with Tkinter and includes a data table that displays the outcome of the action and whether it was a success or failure.
Changes Made

In this version of the code, a separate class for the probability system has been created and the GameLogic class has been updated to use it. This allows for better maintainability, updateability, and extensibility of the codebase. The ProbabilityCalculator class has also been updated to use the new Probability class. This makes the codebase more readable and easy to understand.
Usage

To use the system, run the main() function. The GUI will display buttons for different actions (e.g. "attack", "defend", "cast spell"). Pressing one of the buttons will simulate the outcome of the action and display it in the GUI. The outcome is determined by a roll of a virtual 16-sided die and a comparison with the probability of success for that action.
Note

Please note that the current code is not complete, it is just a part of it. It may contain errors or missing parts that are needed to run the code. You may need to update the code and add missing parts or fix errors before running the code.