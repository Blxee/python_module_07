from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.Card import Card


class GameEngine:
    def __init__(self):
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.available_type: list[Card] = [
            factory.create_creature("dragon"),
            factory.create_creature("goblin"),
            factory.create_spell("fireball"),
            factory.create_artifact("mana_ring"),
        ]

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.__class__.__name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
