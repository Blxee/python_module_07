from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Main function"""
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    available_mana = 6
    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon.is_playable(available_mana))
    print("Play result:", fire_dragon.play({"available_mana": available_mana}))

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard("Goblin Warrior", 4, "common", 2, 3)
    print("Attack result:", fire_dragon.attack_target(goblin))

    available_mana = 3
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(available_mana))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error)
