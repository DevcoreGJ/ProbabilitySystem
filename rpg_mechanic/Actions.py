import random


class Actions:
    def __init__(self):
        self.actions = {"attack": 0.8, "defend": 0.6, "cast spell": 0.9, "use skill": 0.7, "heal": 0.5, "flee": 0.5,}

    def get_actions(self):
        return self.actions.keys()

    def get_action(self, action):
        return self.actions.get(action)
