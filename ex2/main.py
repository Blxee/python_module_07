from ex2.EliteCard import EliteCard, Rarity


def main() -> None:
    """Test the elitecard."""
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")

    arcane_warrior: EliteCard = EliteCard(
        "Arcane Warrior", 4, "rare", 5, 3, 10
    )
    enemy: EliteCard = EliteCard("Enemy", 2, Rarity.COMMON.value, 3, 1, 4)
    # print methods of each of card, magical, combatant
    interfaces = type(arcane_warrior).__bases__
    for base in interfaces:
        methods = [
            name
            for name, attr in vars(base).items()
            if callable(attr) and not name.startswith("__")
        ]
        print(f"- {base.__name__}: {methods}")
    # try combat methods
    print(f"\nPlaying {arcane_warrior.name} (Elite Card):")
    print("\nCombat phase:")
    print("Attack result:", arcane_warrior.attack(enemy))
    print("Defense result:", arcane_warrior.defend(5))

    # try magical methods
    print("\nMagic phase:")
    enemy1: EliteCard = EliteCard("Enemy1", 2, "common", 3, 1, 4)
    enemy2: EliteCard = EliteCard("Enemy2", 2, "common", 3, 1, 4)
    print(
        "Spell cast:", arcane_warrior.cast_spell("Fireball", [enemy1, enemy2])
    )
    print("Mana channel:", arcane_warrior.channel_mana(3))
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error)
