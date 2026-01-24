from abc import ABC, abstractmethod
from typing import Dict

from ex0.CreatureCard import CreatureCard


class Combatable(ABC):
    """Abstract interface for all combatable cards."""

    @abstractmethod
    def attack(self, target: CreatureCard) -> Dict:
        """Abstract method to attack with this card."""
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """Abstract method to defend with this card."""
        ...

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """Abstract method to get combat stats of this card."""
        ...
