from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():
    print('=== DataDeck Game Engine ===\n')
    engine = GameEngine()
    engine.configure_engine(
        factory=FantasyCardFactory(),
        strategy=AggressiveStrategy()
    )

    print('')
    engine.simulate_turn()

    status = engine.get_engine_status()
    print(f'\nGame Report: {status}')

    print('')
    print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')


if __name__ == '__main__':
    main()