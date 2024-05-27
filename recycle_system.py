class RecyclingSystem:
    REWARD_VALUES = {
        'A': 0.10,
        'B': 0.05,
        'C': 0.15
    }
    
    def __init__(self):
        self.items = []
        self.total_reward = 0.0

    def add_item(self, item_type):
        if item_type in self.REWARD_VALUES:
            self.items.append(item_type)
            self.total_reward += self.REWARD_VALUES[item_type]

    def get_total_reward(self):
        return self.total_reward

    def reset(self):
        self.items = []
        self.total_reward = 0.0
