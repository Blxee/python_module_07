from abc import ABC


class GameStrategy(ABC):
    """Abstract superclass for all game strategies."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute turn of the given hand on the battlefield."""
        ...

    execute_turn.__isabstractmethod__ = True

    def get_strategy_name(self) -> str:
        """Retrieve strategy name."""
        ...

    get_strategy_name.__isabstractmethod__ = True

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize using strategy."""
        ...

    prioritize_targets.__isabstractmethod__ = True
