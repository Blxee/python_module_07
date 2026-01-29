from typing import Optional, Dict, List
from ex0.Card import Card, CardType
from enum import Enum
from sys import stderr
from ex0.CreatureCard import CreatureCard


class EffectType(Enum):
    """Enum with possible effect variants."""

    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"

    @staticmethod
    def get_effect_message(
        value: str, amount: int, attribute: Optional[str] = None
    ):
        """Get correct message of each effect."""
        match value:
            case EffectType.DAMAGE.value:
                return f"Deal {amount} damage to target"
            case EffectType.HEAL.value:
                return f"Heal {amount} of target's health"
            case EffectType.BUFF.value:
                return f"Buff {attribute} of target by {amount}"
            case EffectType.DEBUFF.value:
                return f"Debuff {attribute} of target by {amount}"
            case _:
                return "No such effect"


class SpellCard(Card):
    """Playing card for spell specialization."""

    type: CardType = CardType.SPELL

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Create a new SpellCard."""
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str):
            print(
                f"[Error]: invalid type for {self.__class__.__name__}.",
                file=stderr,
            )
            exit(1)
        self.effect_type: str = effect_type
        self.consumed: bool = False

    def play(self, game_state: Dict) -> Dict:
        """Play this spell card using game state."""
        if not isinstance(game_state, dict):
            print("[Error]: invalid argument type to play.", file=stderr)
            exit(1)

        if self.consumed:
            return {"effect": "Spell was already consumed"}

        available_mana = game_state.get("available_mana", 0)
        if available_mana < self.cost:
            return {"effect": "No enough mana to cast spell"}

        self.consumed = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": EffectType.get_effect_message(
                self.effect_type, self.cost
            ),
        }

    def resolve_effect(self, targets: List[CreatureCard]) -> Dict:
        """Apply this spell to the targets in list."""
        if not isinstance(targets, list) or any(
            (not isinstance(target, CreatureCard) for target in targets)
        ):
            print(
                "[Error]: invalid argument type for resolve_effect.",
                file=stderr,
            )
            exit(1)
        return {
            "effects": [
                f"{target.name} was effected by {self.effect_type}"
                for target in targets
            ],
        }
