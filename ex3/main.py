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
    print("Strategy:", game_engine.strategy.__class__.__name__)
    print("Available types:", game_engine.factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    simulation_result = game_engine.simulate_turn()

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
"""

=== DataDeck Game Engine ===

Configuring Fantasy Card Game...
Factory: FantasyCardFactory
Strategy: AggressiveStrategy
Available types: {'creatures': ['dragon', 'goblin'], 'spells': ['fireball'],
'artifacts': ['mana_ring']}

Simulating aggressive turn...
Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]

Turn execution:
Strategy: AggressiveStrategy
Actions: {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
'mana_used': 5, 'targets_attacked': ['Enemy Player'],
'damage_dealt': 8}

Game Report:
{'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy',
'total_damage': 8, 'cards_created': 3}

Abstract Factory + Strategy Pattern: Maximum flexibility achieved!
"""
