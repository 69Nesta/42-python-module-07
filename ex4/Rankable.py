from abc import ABC, abstractmethod


class Rankable(ABC):
    def __init__(self, default_rating: int) -> None:
        self._wins = 0
        self._losses = 0
        self._rating = default_rating

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
