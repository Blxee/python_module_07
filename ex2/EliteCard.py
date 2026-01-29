from typing import Dict, List, Union
from ex0.Card import Card, CardType
from ex2.Magical import Magical
from ex2.Combatable import Combatable
from sys import stderr


class EliteCard(Card, Combatable, Magical):
    """Special cards which is combatable and magical."""
    type: CardType = CardType.ELITE

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        defense: int,
        health: int,
    ) -> None:
        """Constructor for EliteCard class."""
        super().__init__(name, cost, rarity)
        if (
            not isinstance(damage, int)
            or not isinstance(health, int)
            or not isinstance(defense, int)
        ):
            print(
                "[Error]: invalid argument "
                f"type to {self.__class__.__name__}.",
                file=stderr,
            )
            exit(1)
        if damage < 0 or health < 0 or defense < 0:
            print(
                "[Error]: attack, health and defense must be positive.",
                file=stderr,
            )
            exit(1)
        self.damage: int = damage
        self.defense: int = defense
        self.health: int = health
        self.total_mana: int = cost * 2

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
                "effect": "EliteCard summoned to battlefield",
            }
        else:
            return {
                "effect": "Not enough mana to summon EliteCard",
            }

    def attack(self, target: Union[Combatable, Card]) -> Dict:
        """Abstract method to attack with this card."""
        if not isinstance(target, Card) or not isinstance(target, Combatable):
            print("[Error]: invalid argument type to attack()", file=stderr)
            exit(1)
        _ = target.defend(self.damage)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict:
        """Abstract method to defend with this card."""
        if not isinstance(incoming_damage, int):
            print("[Error]: invalid argument type to defend()", file=stderr)
            exit(1)
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = min(self.health, incoming_damage - damage_blocked)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> Dict:
        """Abstract method to get combat stats of this card."""
        return {
            "attack": self.damage,
            "defense": self.defense,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Abstract method for casting this card's spell."""
        if not isinstance(spell_name, str) or not isinstance(targets, list):
            print(
                "[Error]: invalid argument type to cast_spell()", file=stderr
            )
            exit(1)
        for target in targets:
            if not isinstance(target, Card) or not isinstance(
                target, Combatable
            ):
                print(
                    "[Error]: invalid argument type to cast_spell()",
                    file=stderr,
                )
                exit(1)
        if self.total_mana < self.cost:
            return {"error": "no enough mana to cast spell"}
        self.total_mana -= self.cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [target.name for target in targets],
            "mana_used": self.cost,
        }

    def channel_mana(self, amount: int) -> Dict:
        """Abstract method for channeling mana with card."""
        if not isinstance(amount, int):
            print(
                "[Error]: invalid argument type to channel_mana()", file=stderr
            )
            exit(1)
        self.total_mana += amount
        return {"channeled": amount, "total_mana": self.total_mana}

    def get_magic_stats(self) -> Dict:
        """Abstract method to get stats of this magical card."""
        return {
            "total_mana": self.total_mana,
            "cost_per_cast": self.cost,
        }
