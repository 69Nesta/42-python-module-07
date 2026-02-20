from .Card import Card


class CreatureCard(Card):
    def __init__(
                self,
                name: str,
                cost: int,
                rarity: str,
                attack: int,
                health: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health

    def set_attack(self, attack: int) -> None:
        if not isinstance(attack, int):
            raise TypeError('Attack value must be an integer.')
        elif attack < 0:
            raise ValueError('Attack value cannot be negative.')
        self._attack = attack

    def set_health(self, health: int) -> None:
        if not isinstance(health, int):
            raise TypeError('Health value must be an integer.')
        elif health < 0:
            raise ValueError('Health value cannot be negative.')
        self._health = health

    def get_attack(self) -> int:
        return self._attack

    def get_health(self) -> int:
        return self._health

    def remove_health(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Damage amount must be an integer.')
        elif amount < 0:
            raise ValueError('Damage amount cannot be negative.')
        self._health = max(0, self._health - amount)

    def remove_attack(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Attack reduction amount must be an integer.')
        elif amount < 0:
            raise ValueError('Attack reduction amount cannot be negative.')
        self._attack = max(0, self._attack - amount)

    def add_health(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Healing amount must be an integer.')
        elif amount < 0:
            raise ValueError('Healing amount cannot be negative.')
        self._health += amount

    def add_attack(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError('Attack increase amount must be an integer.')
        elif amount < 0:
            raise ValueError('Attack increase amount cannot be negative.')
        self._attack += amount

    def get_card_info(self):
        return super().get_card_info() | {
            'type': 'Creature',
            'attack': self.get_attack(),
            'health': self.get_health()
        }

    def play(self, game_state: dict) -> dict[str, str | int] | None:
        self.use_card(game_state)

        self.on_board = True
        return {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: 'CreatureCard') -> dict:
        target.set_health(max(0, target.get_health() - self.get_attack()))

        return {
            'attacker': self.get_name(),
            'target': target.get_name(),
            'damage_dealt': self.get_attack(),
            'combat_resolved': target.get_health() == 0
        }
