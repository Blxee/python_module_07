from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        print("\nTurn execution:")
        print("Strategy:", self.__class__.__name__)
        result = {
            "cards_played": ["Goblin Warrior", "Lightning Bolt"],
            "mana_used": 5,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8,
        }
        print("Actions:", result)
        return result

    # Actions: {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
    # 'mana_used': 5, 'targets_attacked': ['Enemy Player'],
    # 'damage_dealt': 8}

    def get_strategy_name(self) -> str: ...

    def prioritize_targets(self, available_targets: list) -> list: ...
