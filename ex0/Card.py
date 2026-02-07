from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = 'common'
    UNCOMMON = 'uncommon'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.set_name(name)
        self.set_cost(cost)
        self.set_rarity(rarity)
        self.on_board = False

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        elif not name.strip():
            raise ValueError('Name cannot be empty.')
        self._name = name.strip().lower()

    def set_cost(self, cost: int) -> None:
        if not isinstance(cost, int):
            raise TypeError('Cost must be an integer.')
        elif cost < 0:
            raise ValueError('Cost cannot be negative.')
        self._cost = cost

    def set_rarity(self, rarity: str) -> None:
        if not isinstance(rarity, str):
            raise TypeError('Invalid rarity type. Must be a Rarity enum value')
        try:
            Rarity(rarity.lower())
            self._rarity = rarity.lower()
        except ValueError:
            raise ValueError('Invalid rarity value. Must be one of: ' +
                             ', '.join([r.value for r in Rarity]))

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> int:
        return self._cost

    def get_rarity(self) -> str:
        return self._rarity

    def get_card_info(self) -> dict:
        return {
            'name': self.get_name(),
            'cost': self.get_cost(),
            'rarity': self.get_rarity()
        }

    def is_playable(self, available_mana: int) -> bool:
        return self.get_cost() <= available_mana

    @abstractmethod
    def play(self, game_state: dict) -> dict[str, str | int] | None:
        pass
