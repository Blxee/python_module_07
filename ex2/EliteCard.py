from typing import Dict, List
from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: Dict) -> Dict:
        ...

    def attack(self, target: CreatureCard) -> Dict:
        """Abstract method to attack with this card."""
        ...

    def defend(self, incoming_damage: int) -> Dict:
        """Abstract method to defend with this card."""
        ...

    def get_combat_stats(self) -> Dict:
        """Abstract method to get combat stats of this card."""
        ...

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Abstract method for casting this card's spell."""
        ...

    def channel_mana(self, amount: int) -> Dict:
        """Abstract method for channeling mana with card."""
        ...

    def get_magic_stats(self) -> Dict:
        """Abstract method to get stats of this magical card."""
        ...
