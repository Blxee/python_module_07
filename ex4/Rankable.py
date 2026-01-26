from abc import ABC, abstractmethod


class Rankable(ABC):
    """Interface for all rankables."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate rating based on wins/losses."""
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the wins of this rankable."""
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the losses of this rankable."""
        ...

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Get the info of rankable info ranking you know."""
        ...
