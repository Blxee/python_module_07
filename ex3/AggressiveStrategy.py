from random import choice
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy of aggressive nature :(."""

    def execute_turn(
        self, hand: list[Card], battlefield: list[CreatureCard]
    ) -> dict:
        """Execute turn of the given hand on the battlefield."""
        print("\nTurn execution:")
        print("Strategy:", self.get_strategy_name())
        damage_dealt: int = 0
        mana_used: int = 0

        targets: list[Card] = self.prioritize_targets(battlefield)
        for card in hand:
            play_result: dict = card.play({"available_mana": 42})
            mana_used += play_result.get("mana_used", 0)
            if targets[0].health <= 0:
                del targets[0]
            if len(targets) == 0:
                break
            random_target = targets[0]
            if isinstance(card, Combatable):
                attack_result: dict = card.attack(random_target)
                damage_dealt += attack_result.get("damage", 0)
            elif isinstance(card, CreatureCard):
                attack_result: dict = card.attack_target(random_target)
                damage_dealt += attack_result.get("damage_dealt", 0)

        result = {
            "cards_played": [card.name for card in hand],
            "mana_used": mana_used,
            "targets_attacked": [card.name for card in battlefield],
            "damage_dealt": damage_dealt,
        }

        print("Actions:", result)
        return result

    def get_strategy_name(self) -> str:
        """Retrieve strategy name."""
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        def filter_key(card: Card) -> bool:
            return isinstance(card, (Combatable, CreatureCard))

        def sorting_key(card: Card):
            return card.cost

        return sorted(
            list(filter(filter_key, available_targets)),
            key=sorting_key,
        )
