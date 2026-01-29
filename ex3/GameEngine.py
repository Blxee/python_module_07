from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.Deck import Deck
from random import randint


class GameEngine:
    def __init__(self):
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.deck: Deck = Deck()

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        for lst in factory.create_themed_deck(3).values():
            for card in lst:
                self.deck.add_card(card)
                self.cards_created += 1

    def simulate_turn(self) -> dict:
        hand: list[str] = [
            f"{card.name} ({card.cost})" for card in self.deck.cards
        ]
        print("Hand:", str(hand).replace("'", ""))
        targets: list[Card] = [
            self.factory.create_creature() for i in range(randint(1, 4))
        ]
        self.cards_created += len(targets)
        turn_result: dict = self.strategy.execute_turn(
            self.deck.cards,
            targets,
        )
        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)
        return turn_result

    def get_engine_status(self) -> dict:
        pass
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.__class__.__name__,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
