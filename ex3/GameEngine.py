from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.Deck import Deck


class GameEngine:
    def __init__(self):
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.deck: Deck = Deck()

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        for lst in factory.create_themed_deck(3).values():
            for card in lst:
                self.deck.add_card(card)

    def simulate_turn(self) -> dict:
        hand: list[str] = [
            f"{card.name} ({card.cost})" for card in self.deck.cards
        ]
        print("Hand:", str(hand).replace("'", ""))
        self.strategy.execute_turn(hand, [])

    def get_engine_status(self) -> dict:
        pass
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.__class__.__name__,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
