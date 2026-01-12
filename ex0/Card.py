from abc import ABC, abstractmethod


class Card(ABC):
    """Base class for all cards"""
    type: str

    def __init__(self, name: str, cost: int, rarity: str):
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract method to play the card"""
        pass

    def get_card_info(self) -> dict:
        """Get handy attributes of the card"""
        return {**vars(self), "type": self.type}

    def is_playable(self, available_mana: int) -> bool:
        """Determine whether the card is playable given the available mana"""
        return self.cost <= available_mana
