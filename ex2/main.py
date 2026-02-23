from ex0.Card import Rarity
from .EliteCard import EliteCard


def main() -> None:
    card = EliteCard(
        name='Arcane Warrior',
        cost=5,
        rarity=Rarity.LEGENDARY.value,
        health=10,
        attack_damage=5,
        has_sheild=True,
        combat_type='melee',
        mana=8
    )

    enemys = [
        EliteCard(
            name='Enemy1',
            cost=5,
            rarity=Rarity.RARE.value,
            attack_damage=3,
            health=8,
            has_sheild=True,
            combat_type='ranged',
            mana=2
        ),
        EliteCard(
            name='Enemy2',
            cost=4,
            rarity=Rarity.COMMON.value,
            attack_damage=4,
            health=9,
            has_sheild=False,
            combat_type='melee',
            mana=3
        )
    ]

    capabilities: dict = {}
    for base in reversed(EliteCard.__mro__):
        for name, attr in base.__dict__.items():
            if getattr(attr, "__isabstractmethod__", False):
                capabilities.update({
                    base.__name__: capabilities.get(base.__name__, []) + [name]
                })

    print('=== DataDeck Ability System ===\n')
    print('EliteCard capabilities:')
    for base, methods in capabilities.items():
        print(f'- {base}: {methods}')

    print('\nPlaying Arcane Warrior (Elite Card):\n')
    print('Combat phase:')
    enemy = enemys[0]
    attack_result = card.attack(enemy)
    print(f'Attack result: {attack_result}')
    defense_result = enemy.defend(attack_result.get('damage', 0))
    print(f'Defense result: {defense_result}')

    print('\nMagic phase:')
    spell_result = card.cast_spell('Fireball', enemys)
    print(f'Spell cast: {spell_result}')
    mana_result = card.channel_mana(3)
    print(f'Mana channel: {mana_result}')

    print('\nMultiple interface implementation successful!')


if __name__ == '__main__':
    main()
