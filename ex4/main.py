from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def get_interfacres(cls: TournamentCard) -> list[str]:
    return [base.__name__ for base in cls.__class__.__bases__]


def print_card_info(card: TournamentCard) -> None:
    interfaces = get_interfacres(card)
    print(f'{card.get_name().title()} (ID: {card._id}):')
    print(f'- Interfaces: {interfaces}')
    print(f'- Rating: {card.calculate_rating()}')
    print(f'- Record: {card._wins}-{card._losses}\n')


def main() -> None:
    print('=== DataDeck Tournament Platform ===\n')

    print('Registering Tournament Cards...\n')
    card1 = TournamentCard('dragon_001', 'Fire Dragon', 10, 20, True, 1200)
    print_card_info(card1)
    card2 = TournamentCard('wizard_001', 'Ice Wizard', 10, 20, False, 1150)
    print_card_info(card2)

    print('Creating tournament match...')
    platform = TournamentPlatform()
    platform.register_card(card1)
    platform.register_card(card2)
    match_result = platform.create_match('dragon_001', 'wizard_001')
    print(f'Match result: {match_result}\n')

    print('Tournament Leaderboard:')
    leaderboard = platform.get_leaderboard()
    for idx, card in enumerate(leaderboard, start=1):
        print(f'{idx}. {card.get_name().title()} - ', end='')
        print(f'Rating: {card._rating} ({card._wins}-{card._losses})')

    print('\nPlatform Report:')
    print(platform.generate_tournament_report())

    print('\n=== Tournament Platform Successfully Deployed! ==='
          '\nAll abstract patterns working together harmoniously!')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'An error occurred: {e}')
