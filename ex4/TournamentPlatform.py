from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches: list[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError('Only TournamentCard instances can be registered')
        if card._id in self._cards:
            raise ValueError('Card with this ID is already registered')
        self._cards.update({card._id: card})

        return card._id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)

        if not card1 or not card2:
            raise ValueError('Both cards must be registered to create a match')

        current_player: int = 0
        players: list[TournamentCard] = [card1, card2]
        still_playing: bool = True
        last_damage: int = 0

        while still_playing:
            current_card = players[current_player]
            opponent_card = players[1 - current_player]

            play_result = current_card.play({
                'opponent': opponent_card,
                'incoming_damage': last_damage
            })
            current_player = 1 - current_player
            last_damage = play_result.get('incoming_damage', 0)

            if not play_result.get('still_alive'):
                still_playing = False

        winner_card = players[current_player]
        looser_card = players[1 - current_player]

        winner_card.update_wins(1)
        looser_card.update_losses(1)

        match_result = {
            'winner': winner_card.get_name(),
            'looser': looser_card.get_name(),
            'winner_rating': winner_card.calculate_rating(),
            'loser_rating': looser_card.calculate_rating(),
        }

        self._matches.append(match_result)

        return match_result

    def get_leaderboard(self) -> list:
        cards = list(self._cards.values())
        cards.sort(key=lambda c: c.calculate_rating(), reverse=True)

        return cards

    def generate_tournament_report(self) -> dict:
        cards = list(self._cards.values())

        avg_rating = sum(
            card.calculate_rating()
            for card in cards
        ) // len(cards) if cards else 0

        return {
            'total_cards': len(cards),
            'matches_played': len(self._matches),
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
