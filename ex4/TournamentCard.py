from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from sys import stderr


class TournamentCard(Card, Combatable, Rankable):
    """A special combatable and rankable card."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        defense: int,
        health: int,
        base_rating: int = 0,
        record: tuple[int, int] = (0, 0),
    ) -> None:
        """Create a new tournament card."""
        super().__init__(name, cost, rarity)
        if (
            not isinstance(damage, int)
            or not isinstance(health, int)
            or not isinstance(defense, int)
            or not isinstance(base_rating, int)
            or not isinstance(record, tuple)
            or any(not isinstance(i, int) for i in record)
        ):
            print(
                f"[Error]: invalid argument type to {self.__class__.__name__}",
                file=stderr,
            )
            exit(1)
        if (
            damage < 0
            or health < 0
            or defense < 0
            or any(i < 0 for i in record)
        ):
            print(
                "[Error]: attack, health, defense and record must be positive",
                file=stderr,
            )
            exit(1)

        self.damage: int = damage
        self.defense: int = defense
        self.health: int = health
        self.base_rating: int = base_rating
        self.record: tuple[int, int] = record

    def play(self, game_state: dict) -> dict:
        """Play the card using the current game stats."""
        if not isinstance(game_state, dict):
            print("[Error]: invalid argument type to play.", file=stderr)
            exit(1)
        available_mana = game_state.get("available_mana", 0)

        if self.is_playable(available_mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"{self.name} summoned to battlefield",
            }
        else:
            return {
                "effect": "Not enough mana to summon creature",
            }

    def attack(self, target: "TournamentCard") -> dict:
        """Attack target with this card."""
        if not isinstance(target, TournamentCard):
            print("[Error]: invalid argument type to attack()", file=stderr)
            exit(1)
        defense_result = target.defend(self.damage)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": "melee",
            "target_alive": defense_result["still_alive"],
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend with this card."""
        if not isinstance(incoming_damage, int):
            print("[Error]: invalid argument type to defend()", file=stderr)
            exit(1)
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = min(self.health, incoming_damage - damage_blocked)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        """Get combat stats of this card."""
        return {
            "attack": self.damage,
            "defense": self.defense,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        """Calculate the rating of this card based on wins/losses."""
        wins, losses = self.record
        return self.base_rating + wins * 16 - losses * 16

    def get_tournament_stats(self) -> dict:
        """Retrieve stats of tournament."""
        return {
            "rating": self.calculate_rating(),
            "record": self.record,
        }

    def update_wins(self, wins: int) -> None:
        """Update the wins of this rankable."""
        if not isinstance(wins, int):
            print("[Error]: wins must be an integer.", file=stderr)
            exit(1)
        old_wins, losses = self.record
        self.record = (old_wins + wins, losses)

    def update_losses(self, losses: int) -> None:
        """Update the losses of this rankable."""
        if not isinstance(losses, int):
            print("[Error]: losses must be an integer.", file=stderr)
            exit(1)
        wins, old_losses = self.record
        self.record = (wins, old_losses + losses)

    def get_rank_info(self) -> dict:
        """Get the info of rankable info ranking you know."""
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.record[0],
            "losses": self.record[1],
        }
