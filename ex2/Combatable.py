from abc import ABC, abstractmethod


class Combatable(ABC):
    COMBAT_TYPES = ['melee', 'ranged']

    def __init__(
            self,
            health: int,
            has_sheild: bool,
            attack_damage: int,
            combat_type: str,
            ) -> None:
        self._set_health(health)
        self._set_has_sheild(has_sheild)
        self._set_attack(attack_damage)
        self._set_combat_type(combat_type)

    def _set_combat_type(self, combat_type: str) -> None:
        if (combat_type not in self.COMBAT_TYPES):
            raise ValueError('Invalid attack type. Must be one of: ' +
                             ', '.join(self.COMBAT_TYPES))
        self._combat_type = combat_type

    def _set_attack(self, attack: int) -> None:
        if not isinstance(attack, int):
            raise TypeError('Attack value must be an integer.')
        elif attack < 0:
            raise ValueError('Attack value cannot be negative.')
        self._attack = attack

    def _set_health(self, health: int) -> None:
        if not isinstance(health, int):
            raise TypeError('Health value must be an integer.')
        elif health < 0:
            raise ValueError('Health value cannot be negative.')
        self._health = health

    def _set_has_sheild(self, has_sheild: bool) -> None:
        if not isinstance(has_sheild, bool):
            raise TypeError('has_sheild must be a boolean value.')
        self._has_sheild = has_sheild

    def get_combat_type(self) -> str:
        return self._combat_type

    def get_attack(self) -> int:
        return self._attack

    def get_health(self) -> int:
        return self._health

    def has_sheild(self) -> bool:
        return self._has_sheild

    def _remove_health(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Health amount must be an integer.')
        elif amount < 0:
            raise ValueError('Health amount cannot be negative.')
        self._health = max(0, self._health - amount)

    def _add_health(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Healing amount must be an integer.')
        elif amount < 0:
            raise ValueError('Healing amount cannot be negative.')
        self._health += amount

    @abstractmethod
    def attack(self, target: 'Combatable') -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
