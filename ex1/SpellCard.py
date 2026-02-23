from enum import Enum
from ex0 import Card, CreatureCard


class SpellEffect(Enum):
    DAMAGE = 'damage'
    HEAL = 'heal'
    BUFF = 'buff'
    DEBUFF = 'debuff'


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str
        self.set_effect_type(effect_type)
        self.consumed: bool = False

    def set_effect_type(self, effect_type: str) -> None:
        effect_type = effect_type.strip().lower()
        if effect_type not in SpellEffect._value2member_map_:
            raise ValueError(f'Invalid effect type: {effect_type}')
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if self.consumed:
            raise ValueError(f'{self.get_name()} has already been consumed')
        self.use_card(game_state)

        effect: str
        match self.effect_type:
            case 'damage':
                effect = f'Deal {self.get_cost()} damage to target'
            case 'heal':
                effect = f'Heal {self.get_cost()} health to target'
            case 'buff':
                effect = f'Give target +{self.get_cost()} attack damage ' + \
                         'until end of turn'
            case 'debuff':
                effect = f'Give target -{self.get_cost()} attack damage ' + \
                         'until end of turn'
            case _:
                effect = 'Unknown effect'
        self.consumed = True

        return {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': effect
        }

    def resolve_effect(self, targets: list[CreatureCard]) -> dict:
        for target in targets:
            if not isinstance(target, CreatureCard):
                raise TypeError('Targets must be a CreatureCard instance')

        for target in targets:
            match self.effect_type:
                case 'damage':
                    target.remove_health(self.get_cost())
                case 'heal':
                    target.add_health(self.get_cost())
                case 'buff':
                    target.add_attack(self.get_cost())
                case 'debuff':
                    target.remove_attack(self.get_cost())
        return {
            'card_resolved': self.get_name(),
            'effect_applied': self.effect_type,
            'targets_affected': [target.get_name() for target in targets]
        }
