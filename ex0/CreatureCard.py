from ex0.Card import Card


class CreatureCard(Card):
    """Card of type creature"""
    type: str = "Creature"

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        """Play the card using the current game stats"""
        available_mana = game_state.get("available_mana", 0)

        if self.is_playable(available_mana):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Creature summoned to battlefield",
            }
        else:
            return {
                'effect': "Not enough mana to summon creature",
            }

    def attack_target(self, target: "CreatureCard") -> dict:
        """Make the creature card attack"""
        target.health -= self.attack

        if target.health < 0:
            target.health = 0

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": target.health == 0,
        }
