from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    SPELLS = {
        'fireball': 4
    }

    COMBAT_TYPES = ['melee', 'ranged']

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            health: int,
            has_sheild: bool,
            attack_damage: int,
            combat_type: str,
            mana: int,
            ) -> None:
        super().__init__(name, cost, rarity)
        self._set_health(health)
        self._set_has_sheild(has_sheild)
        self._set_attack(attack_damage)
        self._set_combat_type(combat_type)
        self._set_mana(mana)

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

    def _set_mana(self, mana: int) -> None:
        if not isinstance(mana, int):
            raise TypeError('Mana value must be an integer.')
        elif mana < 0:
            raise ValueError('Mana value cannot be negative.')
        self._mana = mana

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

    def get_mana(self) -> int:
        return self._mana

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

    def play(self, game_state: dict) -> dict:
        players = [
            player
            for player in game_state.get('players', [])
            if player.get_name() != self.get_name()
            and player.get_health() > 0
            and isinstance(player, Combatable)
        ]
        if not players:
            raise ValueError('Game state must include players other '
                             'than the card itself.')

        print(f'Playing {self.get_name().capitalize()} (Elite Card):\n')

        print('Combat phase:')
        attack_result = self.attack(players[0])
        print(f'Attack result: {attack_result}')
        print(f'Defense result: {players[0].defend(attack_result["damage"])}')

        print('\nMagic pase:')
        print(f'Spell cast: {self.cast_spell("fireball", players)}')
        print(f'Mana channel: {self.channel_mana(3)}')

    def attack(self, target: Combatable | Card) -> dict:
        if not isinstance(target, Combatable) or not isinstance(target, Card):
            raise ValueError('Target must be a Combatable Card.')

        return {
            'attacker': self.get_name(),
            'target': target.get_name(),
            'damage': self.get_attack(),
            'combat_type': self.get_combat_type(),
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(
            0,
            incoming_damage - (3 if self.has_sheild() else 0)
        )

        self._remove_health(damage_taken)
        return {
            'defender': self.get_name(),
            'damage_taken': damage_taken,
            'damage_blocked': incoming_damage - damage_taken,
            'still_alive': self.get_health() > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.get_attack(),
            'health': self.get_health(),
            'has_sheild': self.has_sheild(),
            'combat_type': self.get_combat_type()
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_name = spell_name.lower().strip()
        if spell_name not in self.SPELLS:
            raise ValueError('Unknown spell: ' + spell_name)

        mana_cost = self.SPELLS[spell_name]
        if self.get_mana() < mana_cost:
            raise ValueError('Not enough mana to cast ' + spell_name)

        self._remove_mana(mana_cost)
        return {
            'caster': self.get_name(),
            'spell': spell_name,
            'targets': [t.get_name() for t in targets],
            'mana_used': mana_cost,
            'remaining_mana': self.get_mana()
        }

    def channel_mana(self, amount: int) -> dict:
        self._add_mana(amount)

        return {
            'channeled': amount,
            'total_mana': self.get_mana()
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.get_mana(),
            'spells': list(self.SPELLS.keys())
        }
