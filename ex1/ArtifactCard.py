from ex0 import Card


class ArtifactCard(Card):
    EFFECTS_DICT = {
        'mana_boost': 'Permanent: +1 mana per turn',
    }

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._set_duarbility(durability)
        self._set_effect(effect)

    def _set_effect(self, effect: str) -> None:
        if not isinstance(effect, str):
            raise TypeError('Effect must be a string.')

        if effect not in self.EFFECTS_DICT.keys():
            raise ValueError('Effect must be one of'
                             f' {list(self.EFFECTS_DICT.keys())}.')
        self.effect = effect

    def get_effect(self) -> str:
        return self.EFFECTS_DICT[self.effect]

    def _set_duarbility(self, durability: int) -> None:
        if not isinstance(durability, int):
            raise TypeError('Durability must be an integer.')
        elif durability < 0:
            raise ValueError('Durability cannot be negative.')
        self.durability = durability
        self.current_durabiluty = durability

    def _use(self) -> bool:
        if self.current_durabiluty < 1:
            return False
        else:
            self.current_durabiluty -= 1
            return True

    def play(self, game_state: dict) -> dict:
        self.use_card(game_state)

        ability = self.activate_ability()

        return {
            'card_played': ability.get('card_activated'),
            'mana_used': self.get_cost(),
            'effect': ability.get('effect'),
        }

    def activate_ability(self) -> dict:
        if not self._use():
            raise ValueError(f'\'{self.get_name()}\' has no durability '
                             'left to activate its ability.')
        return {
            'card_activated': self.get_name().capitalize(),
            'effect': self.get_effect(),
            'durability_left': self.current_durabiluty
        }
