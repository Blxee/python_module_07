from sys import stderr
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Entry point of the script."""
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    fire_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="legendary",
        damage=8,
        defense=7,
        health=16,
        base_rating=1200,
    )
    ice_wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="rare",
        damage=5,
        defense=2,
        health=8,
        base_rating=1150,
    )

    platform = TournamentPlatform()
    dragon_id: str = platform.register_card(fire_dragon)
    wizard_id: str = platform.register_card(ice_wizard)

    print("\nCreating tournament match...")
    print("Match result:", platform.create_match(dragon_id, wizard_id))

    print("\nTournament Leaderboard:")
    leaderboard: list[str] = platform.get_leaderboard()
    for i, card in enumerate(leaderboard):
        print(f"{i}. {card}")

    print(
        "\nPlatform Report:", platform.generate_tournament_report(), sep="\n"
    )

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
