from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    factory: FantasyCardFactory = FantasyCardFactory()
    strategy: AggressiveStrategy = AggressiveStrategy()
    game_engine: GameEngine = GameEngine()
    game_engine.configure_engine(factory, strategy)

    print("Factory:", game_engine.factory.__class__.__name__)
    print("Strategy:", game_engine.strategy.get_strategy_name())
    print("Available types:", game_engine.factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    _ = game_engine.simulate_turn()

    print("\nGame Report:")
    print(game_engine.get_engine_status())
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    # try:
    main()
# except Exception as error:
#     print("[Error]:", error)
