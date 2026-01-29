from abc import ABC
from typing import Dict, List


class Magical(ABC):
    """Abstract interface for all combatable cards."""

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Abstract method for casting this card's spell."""
        ...

    cast_spell.__isabstractmethod__ = True

    def channel_mana(self, amount: int) -> Dict:
        """Abstract method for channeling mana with card."""
        ...

    channel_mana.__isabstractmethod__ = True

    def get_magic_stats(self) -> Dict:
        """Abstract method to get stats of this magical card."""
        ...

    get_magic_stats.__isabstractmethod__ = True
