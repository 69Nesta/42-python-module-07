from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
                self,
                id: str,
                name: str,
                attack_points: int,
                health_points: int,
                has_sheild: bool,
                default_rating: int = 1000
            ) -> None:
        self._id = id
        Card.__init__(
            self,
            name,
            3,
            Rarity.COMMON.value
        )
        Combatable.__init__(
            self,
            health_points,
            has_sheild,
            attack_points,
            'melee'
        )
        Rankable.__init__(self, default_rating)

    def play(self, game_state: dict) -> dict:
        defend_result = self.defend(game_state.get('incoming_damage', 0))
        still_alive = defend_result.get('still_alive', True)
        if still_alive:
            attack_result = self.attack(game_state.get('opponent', None))

        damages = attack_result.get('damage', 0) if still_alive else 0
        return {
            'played': self.get_name(),
            'defend_result': defend_result,
            'incoming_damage': damages,
            'still_alive': still_alive
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

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            'name': self.get_name(),
            'wins': self._wins,
            'losses': self._losses,
            'rating': self._rating
        }
