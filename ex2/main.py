# === DataDeck Ability System ===

# EliteCard capabilities:
# - Card: ['play', 'get_card_info', 'is_playable']
# - Combatable: ['attack', 'defend', 'get_combat_stats']
# - Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']
#
# Playing Arcane Warrior (Elite Card):
#
# Combat phase:
# Attack result: {'attacker': 'Arcane Warrior', 'target': 'Enemy',
# 'damage': 5, 'combat_type': 'melee'}
# Defense result: {'defender': 'Arcane Warrior', 'damage_taken': 2,
# 'damage_blocked': 3, 'still_alive': True}
#
# Magic phase:
# Spell cast: {'caster': 'Arcane Warrior', 'spell': 'Fireball',
# 'targets': ['Enemy1', 'Enemy2'], 'mana_used': 4}
# Mana channel: {'channeled': 3, 'total_mana': 7}
#
# Multiple interface implementation successful!

from ex0.Card import Rarity, Card
from ex2.EliteCard import EliteCard


def main() -> None:
    card = EliteCard(
        name='Arcane Warrior',
        cost=5,
        rarity=Rarity.LEGENDARY.value,
        health=10,
        attack_damage=5,
        has_sheild=True,
        combat_type='melee',
        mana=4
    )

    # enemys = [
    #     EliteCard(
    #         name='Enemy1',
    #         attack=3,
    #         health=8,
    #         has_sheild=True,
    #         combat_type='ranged',
    #         mana=2
    #     ),
    #     EliteCard(
    #         name='Enemy2',
    #         attack=4,
    #         health=9,
    #         has_sheild=False,
    #         combat_type='melee',
    #         mana=3
    #     )
    # ]

    # game_state = {
    #     'players': [card] + enemys
    # }
    capabilities = {}
    for base in reversed(EliteCard.__mro__):
        for name, attr in base.__dict__.items():
            if getattr(attr, "__isabstractmethod__", False):
                print(f"Found abstract method: {name} in {base.__name__}")
                capabilities.update({
                    base.__name__: capabilities.get(base.__name__, []) + [name]
                })

    print('=== DataDeck Ability System ===\n')
    print('EliteCard capabilities:')
    for base, methods in capabilities.items():
        print(f'- {base}: {methods}')


if __name__ == '__main__':
    main()
