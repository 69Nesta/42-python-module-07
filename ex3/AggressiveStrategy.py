from ex0 import Card, CreatureCard
from ex1 import SpellCard, SpellEffect
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list[Card], battlefield: list[Card]) -> dict:
        prioritize_targets = self.prioritize_targets(battlefield)
        sorted_card_by_cost = sorted(
            hand.copy(),
            key=lambda card: card.get_cost()
        )

        if (not prioritize_targets):
            return {
                'cards_played': [],
                'mana_used': 0,
                'targets_attacked': [],
                'damage_dealt': 0
            }

        selected_cards: list[Card] = []
        total_damage: int = 0

        while len(selected_cards) < 2 and sorted_card_by_cost:
            card = sorted_card_by_cost.pop()
            if isinstance(card, CreatureCard):
                selected_cards.append(card)
                total_damage += card.get_attack()
            elif (isinstance(card, SpellCard)
                  and card.effect_type == SpellEffect.DAMAGE.value):
                selected_cards.append(card)
                total_damage += card.get_cost()

        targets_attacked = [
            target.get_name().title()
            for target in prioritize_targets
        ]

        return {
            'cards_played': [
                card.get_name().title()
                for card in selected_cards
            ],
            'mana_used': sum(card.get_cost() for card in selected_cards),
            'targets_attacked': targets_attacked,
            'damage_dealt': total_damage
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        sorted_targets = sorted(
            [
                target
                for target in available_targets
                if hasattr(target, 'get_health') and target.get_health() > 0
            ],
            key=lambda target: target.get_health(),
        )
        return sorted_targets
