from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: dict) -> dict
    def attack(self, target) -> dict
    def cast_spell(self, spell_name: str, targets: list) -> dict