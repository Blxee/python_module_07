from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
import random
from sys import stderr
from typing import Dict


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        """Create new FantasyCardFactory."""
        self.types: dict[str, dict] = {}
        self.types["creatures"] = {
            "dragon": {
                "names": ["Fire Dragon", "Frost Dragon", "Electro Dragon"],
                "cost_range": range(4, 15),
                "rarities": ["rare", "mythical", "legendary"],
                "attack_range": range(4, 16),
                "health_range": range(8, 25),
            },
            "goblin": {
                "names": [
                    "Goblin Warrior",
                    "Goblin Ranger",
                    "Goblin Sorcerer",
                ],
                "cost_range": range(2, 8),
                "rarities": ["common", "uncommon", "rare"],
                "attack_range": range(1, 7),
                "health_range": range(3, 12),
            },
        }
        self.types["spells"] = {
            "fireball": {
                "names": ["Fire Ball", "Inferno Breath", "Plasma Bolt"],
                "cost_range": range(3, 7),
                "rarities": ["rare", "epic", "legendary"],
                "effect_types": [
                    EffectType.BUFF.value,
                    EffectType.DAMAGE.value,
                    EffectType.DEBUFF.value,
                    EffectType.HEAL.value,
                ],
            }
        }
        self.types["artifacts"] = {
            "mana_ring": {
                "names": ["Mana Ring", "The One Ring", "Mind Control Ring"],
                "cost_range": range(4, 9),
                "rarities": ["rare", "epic", "legendary"],
                "durability_range": range(3, 8),
                "effects": [
                    "Restore Mana",
                    "Paralyze opponents",
                    "Reduce Defense of Opponents",
                ],
            }
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a new random creature."""
        creature = random.choice(list(self.types["creatures"].values()))
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(creature["names"])
        cost = random.choice(creature["cost_range"])
        rarity = random.choice(creature["rarities"])
        if isinstance(name_or_power, int):
            attack = name_or_power
            health = name_or_power
        else:
            attack = random.choice(creature["attack_range"])
            health = random.choice(creature["health_range"])
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a random spell."""
        spell = random.choice(list(self.types["spells"].values()))
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(spell["names"])
        cost = random.choice(spell["cost_range"])
        rarity = random.choice(spell["rarities"])
        effect_type = random.choice(spell["effect_types"])
        print(cost, rarity, effect_type)
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create a random artifact card."""
        artifact = random.choice(list(self.types["artifacts"].values()))
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(artifact["names"])
        cost = random.choice(artifact["cost_range"])
        rarity = random.choice(artifact["rarities"])
        durability = random.choice(artifact["durability_range"])
        effect = random.choice(artifact["effects"])
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        """Create a deck of cards of specific size."""
        cards: dict[str, list] = {}
        for _ in range(size):
            key = random.choice(list(self.types))
            card = None
            match key:
                case "creatures":
                    card = self.create_creature()
                case "spells":
                    card = self.create_spell()
                case "artifacts":
                    card = self.create_artifact()
            if key in cards:
                cards[key].append(card)
            else:
                cards[key] = [card]
        return cards

    def get_supported_types(self) -> dict:
        """Get all the supported types of cards by this factory."""
        return {key: list(val.keys()) for key, val in self.types.items()}

    def register_type(self, card_type: str, name: str, new_type: Dict):
        """Register a new type to be generatable with this factory."""
        if (
            not isinstance(card_type, str)
            or not isinstance(name, str)
            or not isinstance(new_type, dict)
        ):
            print("[Error]: invalid arguments to register_type()", file=stderr)
            return
        if card_type not in ["creatures", "spells", "artifacts"]:
            print(
                "[Error]: there is no such card type:", card_type, file=stderr
            )
            return
        for key in ["names", "cost_range", "rarities"]:
            if key not in new_type:
                print(
                    f"[Error]: {key} is not present in new_type", file=stderr
                )
                return
        if (
            not isinstance(new_type["names"], list)
            or not isinstance(new_type["cost_range"], range)
            or not isinstance(new_type["rarities"], list)
        ):
            print("[Error]: invalid value types in new_type", file=stderr)
            return
        for name in new_type["names"]:
            if not isinstance(name, str):
                print("[Error]: invalid names types in new_type", file=stderr)
                return
        for rarity in new_type["rarities"]:
            if rarity not in [
                "common",
                "uncommon",
                "rare",
                "epic",
                "legendary",
                "mythical",
            ]:
                print(
                    "[Error]: invalid rarities types in new_type", file=stderr
                )
                return
        match card_type:
            case "creatures":
                if not isinstance(
                    new_type.get("attack_range"), range
                ) or not isinstance(new_type.get("health_range"), range):
                    print("[Error]: invalid keys/values in new_type")
                    return
            case "spells":
                if (
                    "effect_types" not in new_type
                    or not isinstance(new_type["effect_types"], list)
                    or not all(
                        e in [et.value for et in EffectType]
                        for e in new_type["effect_types"]
                    )
                ):
                    print("[Error]: invalid keys/values in new_type")
                    return
            case "artifacts":
                if not isinstance(new_type.get("durability_range"), range):
                    print("[Error]: invalid keys/values in new_type")
                    return
                if not isinstance(new_type.get("effects"), list) or any(
                    not isinstance(i, str) for i in new_type["effects"]
                ):
                    print("[Error]: invalid keys/values in new_type")
                    return

        self.types[card_type][name] = new_type
