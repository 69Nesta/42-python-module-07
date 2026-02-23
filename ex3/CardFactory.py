from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    def __init__(self) -> None:
        self._cards_created: int = 0

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

    def increment_created(self) -> None:
        self._cards_created += 1

    def get_cards_created(self) -> int:
        return self._cards_created

    def create_custom_card(self, card: Card) -> Card:
        self.increment_created()
        return card
