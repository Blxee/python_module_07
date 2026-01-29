from ex0.Card import Card, CardType
from sys import stderr
from typing import Dict


class CreatureCard(Card):
    """Card of type creature."""

    type: CardType = CardType.CREATURE

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        """Create a CreatureCard instance."""
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or not isinstance(health, int):
            print(
                "[Error]: invalid argument type"
                f" to {self.__class__.__name__}.",
                file=stderr,
            )
            exit(1)
        if attack < 0 or health < 0:
            print("[Error]: attack and health must be positive.", file=stderr)
            exit(1)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        """Play the card using the current game stats."""
        if not isinstance(game_state, dict):
            print("[Error]: invalid argument type to play.", file=stderr)
            exit(1)
        available_mana = game_state.get("available_mana", 0)

        if self.is_playable(available_mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield",
            }
        else:
            return {
                "effect": "Not enough mana to summon creature",
            }

    def attack_target(self, target: "CreatureCard") -> Dict:
        """Attack the target using the attack damage."""
        if not isinstance(target, CreatureCard):
            print(
                "[Error]: invalid argument type to attack_target.",
                file=stderr,
            )
            exit(1)
        """Make the creature card attack."""
        target.health -= self.attack

        if target.health < 0:
            target.health = 0

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": target.health == 0,
        }
