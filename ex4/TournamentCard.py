from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A special combatable and rankable card."""

    def play(self, game_state: dict) -> dict:
        """Play this card."""
        pass

    def attack(self, target) -> dict:
        """Attack using this card."""
        pass

    def calculate_rating(self) -> int:
        """Calculate the rating of this card based on wins/losses."""
        pass

    def get_tournament_stats(self) -> dict:
        """Retrieve stats of tournament."""
        pass
