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

    def get_card_info(self):
        return super().get_card_info() | {
            'type': 'Creature',
            'attack': self.get_attack(),
            'health': self.get_health()
        }

    def play(self, game_state: dict) -> dict[str, str | int] | None:
        mana_available = game_state.get('available_mana', 0)
        if (self.is_playable(mana_available)):
            game_state.update({
                'available_mana': mana_available - self.get_cost()
            })
            self.on_board = True
            return {
                'card_played': self.get_name(),
                'mana_used': self.get_cost(),
                'effect': 'Creature summoned to battlefield'
            }
        return None

    def attack_target(self, target: 'CreatureCard') -> dict:
        target.set_health(max(0, target.get_health() - self.get_attack()))

        return {
            'attacker': self.get_name(),
            'target': target.get_name(),
            'damage_dealt': self.get_attack(),
            'combat_resolved': target.get_health() == 0
        }
