from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(self, mana: int) -> None:
        self._set_mana(mana)

    def _set_mana(self, mana: int) -> None:
        if not isinstance(mana, int):
            raise TypeError('Mana value must be an integer.')
        elif mana < 0:
            raise ValueError('Mana value cannot be negative.')
        self._mana = mana

    def get_mana(self) -> int:
        return self._mana

    def _remove_mana(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Mana amount must be an integer.')
        elif amount < 0:
            raise ValueError('Mana amount cannot be negative.')
        self._mana = max(0, self._mana - amount)

    def _add_mana(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Mana amount must be an integer.')
        elif amount < 0:
            raise ValueError('Mana amount cannot be negative.')
        self._mana += amount

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
