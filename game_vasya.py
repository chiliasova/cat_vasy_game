from abc import ABC, abstractmethod


class Unit(ABC):
    """Абстрактный базовый класс для всех игровых сущностей."""

    def __init__(
        self,
        strength: int,
        dexterity: int,
        constitution: int,
        wisdom: int,
        intelligence: int,
        charisma: int
    ) -> None:
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma

    @abstractmethod
    def calculate_max_health(self) -> int:
        """Рассчитывает максимальное здоровье."""
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """Рассчитывает урон."""
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """Рассчитывает защиту."""
        pass


class Character(Unit):
    """
    Класс персонажа.
    Может быть: 'warrior', 'mage', 'hunter'.
    """

    def __init__(
        self,
        strength: int,
        dexterity: int,
        constitution: int,
        wisdom: int,
        intelligence: int,
        charisma: int,
        character_class: str
    ) -> None:
        super().__init__(
            strength, dexterity, constitution,
            wisdom, intelligence, charisma
        )

        self.character_class: str = character_class.lower()

        if self.character_class not in ['warrior', 'mage', 'hunter']:
            raise ValueError("Неверный класс персонажа")

        self.max_health: int = self.calculate_max_health()
        self.damage: int = self.calculate_damage()
        self.defense: int = self.calculate_defense()

    def calculate_max_health(self) -> int:
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self) -> int:
        if self.character_class == 'warrior':
            return int(self.strength * 2.2) + self.constitution // 3
        elif self.character_class == 'mage':
            return int(self.intelligence * 2.5) + self.wisdom // 2
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.9) + self.strength // 3
        return 0

    def calculate_defense(self) -> int:
        if self.character_class == 'warrior':
            return int(self.constitution * 1.8) + self.strength // 4
        elif self.character_class == 'mage':
            return int(self.wisdom * 1.3) + self.intelligence // 6
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.6) + self.constitution // 5
        return 0