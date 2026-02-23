from ex0 import Rarity, CreatureCard
from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


def main() -> None:
    print('=== DataDeck Deck Builder ===\n')
    deck = Deck()

    print('Building deck with different card types...')
    deck.add_card(
        CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY.value, 3, 5)
    )
    deck.add_card(
        ArtifactCard('Mana Crystal', 4, Rarity.RARE.value, 1, 'mana_boost')
    )
    deck.add_card(
        SpellCard('Lightning Bolt', 3, Rarity.COMMON.value, 'damage')
    )

    print(f'Deck stats: {deck.get_deck_stats()}')

    game_state: dict[str, int] = {
        'available_mana': 12
    }

    print('\nDrawing and playing cards:\n')
    for _ in range(deck.total_cards()):
        card = deck.draw_card()
        if card:
            print(f'Drew: {card.get_name().capitalize()} '
                  f'({card.__class__.__name__})')
            try:
                result = card.play(game_state)
                print(f'Play result: {result}\n')
            except ValueError as e:
                print(f'Cannot play \'{card.get_name().title()}\': {e}\n')
        else:
            print('Deck is empty!\n')

    print('Polymorphism in action: Same interface, different card behaviors!')


if __name__ == '__main__':
    main()
