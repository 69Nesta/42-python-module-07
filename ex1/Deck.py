from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


from random import shuffle


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError('Only Card instances can be added to the deck.')
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.get_name() == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def total_cards(self) -> int:
        return len(self.cards)

    def get_deck_stats(self) -> dict:
        deck_stats: dict[str, int | float] = {}
        total_cards = len(self.cards)
        avg_cost = sum(card.get_cost() for card in self.cards) / total_cards
        deck_stats.update({
            'total_cards': total_cards,
            'avg_cost': avg_cost
        })

        def incr_cat(name: str):
            deck_stats.update({name: deck_stats.get(name, 0) + 1})

        for card in self.cards:
            if isinstance(card, CreatureCard):
                incr_cat('creatures')
            elif isinstance(card, SpellCard):
                incr_cat('spells')
            elif isinstance(card, ArtifactCard):
                incr_cat('artifacts')

        return deck_stats
