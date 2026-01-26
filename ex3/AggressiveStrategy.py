from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        print("Turn execution:")
        print("Strategy:", self.strategy.__class__.__name__)
# Actions: {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
# 'mana_used': 5, 'targets_attacked': ['Enemy Player'],
# 'damage_dealt': 8}

    def get_strategy_name(self) -> str: ...

    def prioritize_targets(self, available_targets: list) -> list: ...
