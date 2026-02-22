from .CardFactory import CardFactory

from ex0.Card import Rarity, Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, SpellEffect


class FantasyCardFactory(CardFactory):
    SUPPORTED_TYPES: dict[str, list[str]] = {
        'creature': [
            'dragon',
            'goblin'
        ],
        'spell': [
            'fireball'
        ],
        'artifact': [
            'mana_ring'
        ]
    }

    def is_valid_creature_type(
                self,
                name_or_power: str | int | None,
                default_card: str,
                category: str
            ) -> tuple[str, int | None]:
        creature_type: str
        power: int | None = None

        if isinstance(name_or_power, str) \
           and self.SUPPORTED_TYPES.get(category) is not None \
           and name_or_power in self.SUPPORTED_TYPES[category] is not None:
            creature_type = name_or_power
        elif isinstance(name_or_power, int):
            power = name_or_power
        else:
            creature_type = default_card
        return creature_type, power

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature_type, power = self.is_valid_creature_type(
            name_or_power,
            default_card='goblin',
            category='creature'
        )

        match creature_type:
            case 'dragon':
                self.increment_created()
                return CreatureCard(
                    'Fire Dragon',
                    5,
                    Rarity.RARE.value,
                    10,
                    20
                )
            case 'goblin':
                self.increment_created()
                return CreatureCard(
                    'Goblin Warrior',
                    2,
                    Rarity.COMMON.value,
                    power or 2,
                    10
                )

        raise ValueError(f"Unsupported creature name: {name_or_power}")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        creature_type, _ = self.is_valid_creature_type(
            name_or_power,
            default_card='fireball',
            category='spell'
        )

        match creature_type:
            case 'fireball':
                self.increment_created()
                return SpellCard(
                    'Lightning Bolt',
                    3,
                    Rarity.UNCOMMON.value,
                    SpellEffect.DAMAGE.value,
                )

        raise ValueError(f"Unsupported spell name: {name_or_power}")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        creature_type, power = self.is_valid_creature_type(
            name_or_power,
            default_card='mana_ring',
            category='artifact'
        )

        match creature_type:
            case 'mana_ring':
                self.increment_created()
                return ArtifactCard(
                    'Mana Ring',
                    10,
                    Rarity.RARE.value,
                    power or 3,
                    'mana_boost',
                )

        raise ValueError(f"Unsupported spell name: {name_or_power}")

    def create_themed_deck(self, size: int) -> dict:
        deck: dict[str, list[Card]] = {
            'creature': [],
            'spell': [],
            'artifact': []
        }

        ratios = {
            'goblin': 0.3,
            'dragon': 0.3,
            'fireball': 0.3,
            'mana_ring': 0.1,
        }

        counts = {k: int(size * v) for k, v in ratios.items()}
        remaining = size - sum(counts.values())

        for key in counts:
            if remaining == 0:
                break
            counts[key] += 1
            remaining -= 1

        for _ in range(counts['goblin']):
            deck['creature'].append(self.create_creature('goblin'))

        for _ in range(counts['dragon']):
            deck['creature'].append(self.create_creature('dragon'))

        for _ in range(counts['fireball']):
            deck['spell'].append(self.create_spell('fireball'))

        for _ in range(counts['mana_ring']):
            deck['artifact'].append(self.create_artifact('mana_ring'))

        return deck

    def get_supported_types(self) -> dict:
        return self.SUPPORTED_TYPES
