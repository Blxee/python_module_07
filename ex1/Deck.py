from math import ceil
from typing import List, Any, Dict

from ex0.Card import Card
from random import shuffle
from sys import stderr


class Deck:
    def __init__(self) -> None:
        """Create a new deck of cards."""
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a new card to the deck."""
        if not isinstance(card, Card):
            print("[Error]: invalid argument type for add_card().", file=stderr)
            exit(1)
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck using its name."""
        if not isinstance(card_name, str):
            print("[Error]: invalid argument type for remove_card().", file=stderr)
            exit(1)
        for card in self.cards.copy():
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck of cards randomly."""
        shuffle(self.cards)

    def draw_card(self) -> Card:
        """Get the card at the top of the deck."""
        if len(self.cards) == 0:
            print("[Error]: cannot draw from an emtpy deck.")
            exit(1)
        return self.cards.pop()

    def get_deck_stats(self) -> Dict:
        """Return the stats of the current deck of cards."""
        stats: Dict[str, Any] = { "total_cards": len(self.cards) }
        total_cost: float = 0

        for card in self.cards:
            total_cost += card.cost

            card_type: str = f"{card.type.lower()}s"
            if card_type in stats:
                stats[card_type] += 1
            else:
                stats[card_type] = 1

        stats["avg_cost"] = float(ceil(total_cost / len(self.cards)))
        return stats

