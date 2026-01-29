from abc import ABC
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract superclass for all card factories."""

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create the creature for the creature to be created."""
        ...

    create_creature.__isabstractmethod__ = True

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell."""
        ...

    create_spell.__isabstractmethod__ = True

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact."""
        ...

    create_artifact.__isabstractmethod__ = True

    def create_themed_deck(self, size: int) -> dict:
        """Create a random deck of cards of a specific size."""
        ...

    create_themed_deck.__isabstractmethod__ = True

    def get_supported_types(self) -> dict:
        """Get all the supported types of cards this factory can create."""
        ...

    get_supported_types.__isabstractmethod__ = True
