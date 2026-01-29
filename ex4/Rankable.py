from abc import ABC


class Rankable(ABC):
    """Interface for all rankables."""

    def calculate_rating(self) -> int:
        """Calculate rating based on wins/losses."""
        ...

    calculate_rating.__isabstractmethod__ = True

    def update_wins(self, wins: int) -> None:
        """Update the wins of this rankable."""
        ...

    update_wins.__isabstractmethod__ = True

    def update_losses(self, losses: int) -> None:
        """Update the losses of this rankable."""
        ...

    update_losses.__isabstractmethod__ = True

    def get_rank_info(self) -> dict:
        """Get the info of rankable info ranking you know."""
        ...

    get_rank_info.__isabstractmethod__ = True
