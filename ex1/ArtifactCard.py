from typing import Dict
from ex0.Card import Card
from sys import stderr


class ArtifactCard(Card):
    type = "Artifact"

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        """Create a new ArtifactCard."""
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        """Play this artifact card."""
        if not isinstance(game_state, dict):
            print(f"[Error]: invalid argument type to play.", file=stderr)
            exit(1)

        if self.durability <= 0:
            return {"effect": "No enough durability to activate artifact"}

        available_mana = game_state.get("available_mana", 0)
        if available_mana < self.cost:
            return {"effect": "No enough mana to activate artifact"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            **self.activate_ability(),
        }

    def activate_ability(self) -> Dict:
        """Activate this permanent ability for the current match."""
        return {
            "effect": f"Permanent: {self.effect}"
        }

