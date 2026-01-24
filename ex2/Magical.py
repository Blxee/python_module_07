from abc import ABC, abstractmethod
from typing import Dict, List

class Magical(ABC):
    """Abstract interface for all combatable cards."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Abstract method for casting this card's spell."""
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Abstract method for channeling mana with card."""
        ...

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Abstract method to get stats of this magical card."""
        ...
