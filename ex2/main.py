from ex2.EliteCard import EliteCard


def main() -> None:
    """Test the elitecard"""
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    # print methods of each of card, magical, combatant

    arcane_warrior: EliteCard = EliteCard("Arcane Warrior")
    print(f"\nPlaying {arcane_warrior.name} (Elite Card):")
    print("\nCombat phase:")
    print("Attack result:", arcane_warrior.attack())
    print("Defense result:", arcane_warrior.defend())

    print("\nMagic phase:")
    print("Spell cast:", arcane_warrior.cast_spell())
    print("Mana channel:", arcane_warrior.channel_mana())
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error)
"""

=== DataDeck Ability System ===

EliteCard capabilities:
- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']

Playing Arcane Warrior (Elite Card):

Combat phase:
Attack result: {'attacker': 'Arcane Warrior', 'target': 'Enemy',
'damage': 5, 'combat_type': 'melee'}
Defense result: {'defender': 'Arcane Warrior', 'damage_taken': 2,
'damage_blocked': 3, 'still_alive': True}

Magic phase:
Spell cast: {'caster': 'Arcane Warrior', 'spell': 'Fireball',
'targets': ['Enemy1', 'Enemy2'], 'mana_used': 4}
Mana channel: {'channeled': 3, 'total_mana': 7}

Multiple interface implementation successful!
"""
