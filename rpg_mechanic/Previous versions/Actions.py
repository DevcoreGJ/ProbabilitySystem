import random


class Actions:
    def __init__(self):
        self.actions = {"Attack": 0.8, "Defend": 0.6, "Cast Spell": 0.9, "Use Skill": 0.7, "Heal": 0.5, "Flee": 0.5,}

    def get_actions(self):
        return self.actions.keys()

    def get_action(self, action):
        return self.actions.get(action)
