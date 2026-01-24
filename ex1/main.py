from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard, EffectType
import random


def main() -> None:
    """Test the deck of cards with polymorphic usage."""
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    deck: Deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Mythical", 3, "+1 mana per turn"))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", EffectType.DAMAGE))

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")
    # seed the random generator so we get the same order in the example.
    random.seed(129)
    deck.shuffle()
    for i in range(3):
        card: Card = deck.draw_card()
        print(f"\nDrew: {card.name} ({card.type})")
        print("Play result:", card.play({"available_mana": 10}))

    print("\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error)