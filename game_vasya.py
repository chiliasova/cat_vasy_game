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
        