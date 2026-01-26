from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
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
                    EffectType.BUFF,
                    EffectType.DAMAGE,
                    EffectType.DEBUFF,
                    EffectType.HEAL,
                ],
            }
        }
        self.types["mana_ring"] = {
            "names": ["Mana Ring", "The One Ring", "Mind Control Ring"],
            "cost_range": range(4, 9),
            "durability_range": range(3, 8),
            "effects": [
                "Restore Mana",
                "Paralyze opponents",
                "Reduce Defense of Opponents",
            ],
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
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
        spell = random.choice(list(self.types["spells"].values()))
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(spell["names"])
        cost = random.choice(spell["cost_range"])
        rarity = random.choice(spell["rarities"])
        effect_type = random.choice(spell["effect_types"])
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifact = random.choice(list(self.types["mana_ring"].values()))
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
        cards: dict[str, list] = {}
        for _ in range(size):
            key = random.choice(self.types)
            card = None
            match key:
                case "creatures":
                    card = [self.create_creature()]
                case "spells":
                    card = [self.create_spell()]
                case "mana_ring":
                    card = [self.create_artifact()]
            if key in cards:
                cards[key].append(card)
            else:
                cards[key] = [card]
        return cards

    def get_supported_types(self) -> dict:
        return {key: list(val.keys()) for key, val in self.types.items()}
