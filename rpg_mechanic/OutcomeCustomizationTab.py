import tkinter as tk
import os

class OutcomeCustomizationTab:
    def __init__(self, tab, data_table, outcome_weights, default_outcomes):
        self.tab = tab
        self.data_table = data_table
        self.outcome_weights = outcome_weights
        self.default_outcomes = default_outcomes
        self.custom_outcomes_dict = {} # Define custom_outcomes_dict as a class variable

        # Create a button to restore defaults
        self.restore_default_button = tk.Button(self.tab, text="Restore Default", command=self.restore_defaults)
        self.restore_default_button.pack()
        
        # Create a list of current outcomes in the DataTable
        self.outcomes_list = tk.Listbox(self.tab)
        self.update_outcomes_list() # Call the function to populate the list
        self.outcomes_list.pack()

        # Create input fields for users to enter their desired outcomes
        self.custom_outcomes = {}
        self.custom_outcome_weights = {}
        for i in range(len(self.data_table.table)):
            row = tk.Frame(self.tab)
            label = tk.Label(row, width=20, text=f'Roll {i+1}', anchor='w')
            entry = tk.Entry(row)
            weight_entry = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            label.pack(side=tk.LEFT)
            entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
            weight_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
            self.custom_outcomes[i] = entry
            self.custom_outcome_weights[i] = weight_entry

        # Create a save button to save custom outcomes
        save_button = tk.Button(self.tab, text="Save", command=self.save_custom_outcomes)
        save_button.pack()

    def save_custom_outcomes(self):
        for i, entry in self.custom_outcomes.items():
            custom_outcome = entry.get()
            if custom_outcome and custom_outcome.strip():
                self.custom_outcomes_dict[i] = custom_outcome # Add the custom outcome to the dict
                self.data_table.table[i] = custom_outcome
                self.update_outcomes_list()

                # Create a file in the "CustomPresets" folder and save the custom outcomes
                filename = f"CustomPresets/custom_outcomes_{i}.txt"
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, "w") as f:
                    f.write(custom_outcome)
                    
    def restore_defaults(self):
        self.data_table.table = self.default_outcomes.copy()
        for i, default_outcome in enumerate(self.default_outcomes):
            self.data_table.table[i] = default_outcome
            self.outcome_weights.set_weight(default_outcome, 1)
            self.update_outcomes_list()
            self.custom_outcomes_dict = {} # Clear the custom outcomes dict

    def update_outcomes_list(self):
        self.outcomes_list.delete(0, tk.END) #
        
# This function should be called whenever the outcomes in the data_table are updated, so that the list displayed in the UI is also updated.
# This function should also be called in the restore_defaults function, so that the list is updated with the default outcomes.
# The function should clear the current list and then insert all the outcomes in the data_table.
# This way, you will be able to see the custom outcomes and the default outcomes in the list.

