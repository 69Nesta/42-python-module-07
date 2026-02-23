from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    SPELLS = {
        'fireball': 4
    }

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
        Card.__init__(
            self,
            name,
            cost,
            rarity
        )
        Combatable.__init__(
            self,
            health,
            has_sheild,
            attack_damage,
            combat_type
        )
        Magical.__init__(self, mana)

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
        defense_result = players[0].defend(attack_result["damage"])
        print(f'Defense result: {defense_result}')

        print('\nMagic pase:')
        cast_result = self.cast_spell("fireball", players)
        print(f'Spell cast: {cast_result}')
        channel_result = self.channel_mana(3)
        print(f'Mana channel: {channel_result}')

        return {
            'played': self.get_name(),
            'attack_result': attack_result,
            'spell_cast': cast_result,
            'mana_channel': channel_result
        }

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
