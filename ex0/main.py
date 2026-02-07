from .Card import Rarity
from .CreatureCard import CreatureCard


def main() -> None:
    print('=== DataDeck Card Foundation ===\n')
    print('Testing Abstract Base Class Design:\n')

    fire_dragon = CreatureCard(
        name='Fire Dragon',
        cost=5,
        rarity=Rarity.LEGENDARY.value,
        attack=7,
        health=5
    )
    print('CreatureCard Info:')
    print(fire_dragon.get_card_info())
    print()

    available_mana = 6
    print(f'Playing {fire_dragon.get_name()} with {available_mana} '
          'mana available:')
    print(f'Playable: {fire_dragon.is_playable(available_mana)}')
    print('Play result: '
          f'{fire_dragon.play({"available_mana": available_mana})}')
    print()

    goblin_warrior = CreatureCard(
        name='Goblin Warrior',
        cost=2,
        rarity=Rarity.COMMON.value,
        attack=3,
        health=2
    )
    print(f'{fire_dragon.get_name()} attacks {goblin_warrior.get_name()}:')
    print(f'Attack result: {fire_dragon.attack_target(goblin_warrior)}')
    print()

    available_mana = 3
    print(f'Testing insufficient mana ({available_mana} available):')
    print(f'Playable: {fire_dragon.is_playable(available_mana)}')
    print('\nAbstract pattern successfully demonstrated!')


if __name__ == '__main__':
    main()
