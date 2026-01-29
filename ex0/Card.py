from abc import ABC
from sys import stderr
from enum import Enum
from typing import Dict


class CardType(Enum):
    """Enum for different card types."""

    CREATURE = "Creature"
    SPELL = "Spell"
    ELITE = "Elite"
    ARTIFACT = "Artifact"


class Card(ABC):
    """Base class for all cards."""

    type: CardType

    def __init__(self, name: str, cost: int, rarity: str):
        """Create a new Card."""
        if (
            not isinstance(name, str)
            or not isinstance(cost, int)
            or not isinstance(rarity, str)
        ):
            print(
                "[Error]: invalid argument type"
                f" to {self.__class__.__name__}.",
                file=stderr,
            )
            exit(1)
        if cost < 0:
            print("[Error]: mana should be positive", file=stderr)
            exit(1)
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    def play(self, game_state: Dict) -> Dict:
        """Abstract method to play the card."""
        ...

    play.__isabstractmethod__ = True

    def get_card_info(self) -> Dict:
        """Get handy attributes of the card."""
        return {**vars(self), "type": self.type.value}

    def is_playable(self, available_mana: int) -> bool:
        """Determine whether this card is playable based on mana."""
        if not isinstance(available_mana, int):
            print(
                "[Error]: invalid argument type to is_playable.", file=stderr
            )
            exit(1)
        """Determine whether the card is playable given the available mana"""
        return self.cost <= available_mana
