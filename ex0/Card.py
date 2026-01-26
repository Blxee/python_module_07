from abc import ABC, abstractmethod
from sys import stderr


class Card(ABC):
    """Base class for all cards"""

    type: str

    def __init__(self, name: str, cost: int, rarity: str):
        if (
            not isinstance(name, str)
            or not isinstance(cost, int)
            or not isinstance(rarity, str)
        ):
            print(
                f"[Error]: invalid argument type to {self.__class__.__name__}.",
                file=stderr,
            )
            exit(1)
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
        if not isinstance(available_mana, int):
            print(
                "[Error]: invalid argument type to is_playable.", file=stderr
            )
            exit(1)
        """Determine whether the card is playable given the available mana"""
        return self.cost <= available_mana
