from ex4.TournamentCard import TournamentCard
from sys import stderr
from itertools import count
from typing import Any


class TournamentPlatform:
    def __init__(self) -> None:
        """Create a new tournament platform."""
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a new card for tournament."""
        if not isinstance(card, TournamentCard) or len(card.name.strip()) == 0:
            print("[Error]: could not register card", file=stderr)
            exit(1)
        # generate an id string
        for i in count(1):
            card_id = card.name.split()[-1].lower() + f"_{i:03}"
            if card_id not in self.cards:
                break
        # get all the interfaces inhirited
        interfaces = [inter.__name__ for inter in type(card).__bases__]
        interfaces = str(interfaces).replace("'", "")

        print(f"""
{card.name} (ID: {card_id}):
- Interfaces: {interfaces}
- Rating: {card.calculate_rating()}
- Record: {"-".join(map(str, card.record))}""")

        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            print("[Error]: card was not registered yet", file=stderr)
            exit(1)

        attacking: TournamentCard = self.cards[card1_id]
        defending: TournamentCard = self.cards[card2_id]

        attacking_id: str = card1_id
        defending_id: str = card2_id

        for _ in range(100):
            result: dict[str, Any] = attacking.attack(defending)
            # if defending card losses, end the combat
            if not result["target_alive"]:
                break
            # swap turns
            attacking, defending = defending, attacking
            attacking_id, defending_id = defending_id, attacking_id

        attacking.update_wins(1)
        defending.update_losses(1)

        self.matches_played += 1

        return {
            "winner": attacking_id,
            "loser": defending_id,
            "winner_rating": attacking.calculate_rating(),
            "loser_rating": defending.calculate_rating(),
        }

    def get_leaderboard(self) -> list[str]:
        cards = sorted(
            self.cards.values(),
            key=lambda card: card.calculate_rating(),
            reverse=True,
        )
        result: list[str] = []
        for info in [card.get_rank_info() for card in cards]:
            result.append(
                f"{info['name']} - Rating: {info['rating']}"
                f" ({info['wins']}-{info['losses']})"
            )
        return result

    def generate_tournament_report(self) -> dict:
        avg_rating: int = sum(
            card.calculate_rating() for card in self.cards.values()
        ) // len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
