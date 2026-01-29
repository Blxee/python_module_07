from abc import ABC
from typing import Dict

from ex0.CreatureCard import CreatureCard


class Combatable(ABC):
    """Abstract interface for all combatable cards."""

    def attack(self, target: CreatureCard) -> Dict:
        """Abstract method to attack with this card."""
        ...

    attack.__isabstractmethod__ = True

    def defend(self, incoming_damage: int) -> Dict:
        """Abstract method to defend with this card."""
        ...

    defend.__isabstractmethod__ = True

    def get_combat_stats(self) -> Dict:
        """Abstract method to get combat stats of this card."""
        ...

    get_combat_stats.__isabstractmethod__ = True
