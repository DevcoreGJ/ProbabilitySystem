class Weather:
    def __init__(self):
        self.conditions = {
        "Clear": {"Attack": 1.0, "Defend": 1.0, "Cast Spell": 1.0, "Use Skill": 1.0, "Heal": 1.0, "Flee": 1.0},
        "Rain": {"Attack": 0.8, "Defend": 1.2, "Cast Spell": 0.9, "Use Skill": 0.9, "Heal": 1.1, "Flee": 1.0},
        "Snow": {"Attack": 0.6, "Defend": 1.4, "Cast Spell": 0.8, "Use Skill": 0.8, "Heal": 1.2, "Flee": 1.2},
        "Windy": {"Attack": 0.9, "Defend": 1.1, "Cast Spell": 0.8, "Use Skill": 1.0, "Heal": 1.0, "Flee": 1.0},
        "Foggy": {"Attack": 0.7, "Defend": 1.3, "Cast Spell": 0.9, "Use Skill": 0.8, "Heal": 1.1, "Flee": 1.0},
        "Overcast": {"Attack": 0.8, "Defend": 1.2, "Cast Spell": 0.9, "Use Skill": 0.9, "Heal": 1.1, "Flee": 1.0},
        "Thunderstorm": {"Attack": 0.7, "Defend": 1.3, "Cast Spell": 0.8, "Use Skill": 0.9, "Heal": 1.1, "Flee": 1.0},
        "Sandstorm": {"Attack": 0.6, "Defend": 1.4, "Cast Spell": 0.7, "Use Skill": 0.8, "Heal": 1.2, "Flee": 1.0},
        "Hailstorm": {"Attack": 0.5, "Defend": 1.5, "Cast Spell": 0.6, "Use Skill": 0.7, "Heal": 1.3, "Flee": 1.0},
        "Blizzard": {"Attack": 0.4, "Defend": 1.6, "Cast Spell": 0.5, "Use Skill": 0.6, "Heal": 1.4, "Flee": 1.2},
        }
        self.current_condition = "Clear"
        

    def set_weather(self, condition):
        if condition in self.conditions:
            self.current_condition = condition
        else:
            print(f"Invalid weather condition: {condition}")

    def get_probabilities(self):
        return self.conditions[self.current_condition]

