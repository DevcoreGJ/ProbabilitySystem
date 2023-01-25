OutcomeWeights

This is a Python class that simulates rolling for an outcome, based on a set of predefined outcomes and their corresponding weights. The class has methods to normalize the weights, calculate the cumulative probabilities for each outcome, get the weight percentage of a given outcome, roll for an outcome and return it.
Installation

This package does not require any installation. Simply copy the code and use it in your project.
Usage

To use the class, create an instance of the class by calling weights = OutcomeWeights(). This will automatically create the self.weights attribute with the desired outcomes and their weights.

You can then use the following methods on the weights instance:

    normalize_weights(): normalizes the weights by dividing each weight by the total weight
    get_cumulative_probabilities(): creates a dictionary of cumulative probabilities for each outcome
    get_outcome(roll): returns the outcome corresponding to a given roll
    get_weight_percentage(outcome): returns the weight percentage of a given outcome
    roll_outcome(): rolls for an outcome and return it, also print the weight percentage of all outcomes.

You can also change the outcomes and their corresponding weights in the __init__ method.

Example:

weights = OutcomeWeights()
weights.normalize_weights()
outcome = weights.roll_outcome()

This will create an instance of the class, normalize the weights, and roll for an outcome.
Contribution

Please feel free to submit any issues or pull requests if you have any suggestions or improvements.
License

This code is available under the MIT license.