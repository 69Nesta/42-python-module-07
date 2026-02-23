from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard


class GameEngine:
    def __init__(self):
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0

    def configure_engine(
                self,
                factory: CardFactory,
                strategy: GameStrategy
            ) -> None:
        print('Configuring Fantasy Card Game...')
        print(f'Factory: {factory.__class__.__name__}')
        print(f'Strategy: {strategy.__class__.__name__}')
        print(f'Available types: {factory.get_supported_types()}')
        self._factory = factory
        self._strategy = strategy

    def get_factory(self) -> CardFactory:
        if self._factory is None:
            raise ValueError('Factory not configured')
        return self._factory

    def get_strategy(self) -> GameStrategy:
        if self._strategy is None:
            raise ValueError('Strategy not configured')
        return self._strategy

    def _increment_turns(self) -> None:
        self._turns_simulated += 1

    def simulate_turn(self) -> dict:
        print('Simulating aggressive turn...')
        deck: dict[str, list[Card]] = self.get_factory().create_themed_deck(3)

        hand: list[Card] = [card for cards in deck.values() for card in cards]
        battlefield: list[Card] = [
            self.get_factory().create_custom_card(
                CreatureCard('Enemy Goblin', 2, Rarity.COMMON.value, 2, 10)
            )
        ]

        print('Hand: [' +
              ", ".join([
                  f"{card.get_name().title()} ({card.get_cost()})"
                  for card in hand
              ]) +
              ']'
              )

        print('\nTurn execution:')
        print(f'Strategy: {self.get_strategy().get_strategy_name()}')
        turn_actions: dict[str, list | int] = self.get_strategy().execute_turn(
            hand,
            battlefield
        )
        print(f'Actions: {turn_actions}')
        self._increment_turns()
        self._total_damage += turn_actions.get('damage_dealt', 0)

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': self.get_strategy().get_strategy_name(),
            'total_damage': self._total_damage,
            'cards_created': self.get_factory().get_cards_created()
        }
