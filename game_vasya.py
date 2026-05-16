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
        self.spells: list = []
        self.mana: int = 0

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

    def add_spell(self, spell) -> None:
        """Добавляет заклинание в список."""
        self.spells.append(spell)

    def cast_spell(self, index: int):
        """Использует заклинание по индексу."""
        if index < 0 or index >= len(self.spells):
            return None

        spell = self.spells[index]

        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        return None


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
        self.mana: int = self.calculate_max_mana()

    def calculate_max_health(self) -> int:
        return self.constitution * 10 + self.strength // 2

    def calculate_max_mana(self) -> int:
        if self.character_class == 'warrior':
            return self.intelligence + self.strength // 2
        elif self.character_class == 'mage':
            return self.intelligence * 3 + self.wisdom
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.5) + self.wisdom // 2
        return 0

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


class Spell(ABC):
    """Абстрактный класс для заклинаний."""

    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        self.name: str = name
        self.damage: int = damage
        self.mana_cost: int = mana_cost

    @abstractmethod
    def cast(self) -> int:
        """Использовать заклинание, вернуть урон."""
        pass


class Fireball(Spell):
    """Огненный шар."""

    def __init__(self) -> None:
        super().__init__("Огненный шар", 35, 15)

    def cast(self) -> int:
        return self.damage


class IceLance(Spell):
    """Ледяное копьё."""

    def __init__(self) -> None:
        super().__init__("Ледяное копьё", 25, 10)

    def cast(self) -> int:
        return self.damage


class LightningBolt(Spell):
    """Молния."""

    def __init__(self) -> None:
        super().__init__("Молния", 40, 20)

    def cast(self) -> int:
        return self.damage


if __name__ == "__main__":
    print("=" * 50)
    print("ИГРА ОТ КОТА ВАСИЛИЯ")
    print("=" * 50)

    warrior = Character(20, 15, 25, 10, 8, 12, 'warrior')
    mage = Character(8, 12, 10, 20, 25, 15, 'mage')

    print(f"Воин: здоровье={warrior.max_health}, урон={warrior.damage}, "
          f"защита={warrior.defense}, мана={warrior.mana}")
    print(f"Маг: здоровье={mage.max_health}, урон={mage.damage}, "
          f"защита={mage.defense}, мана={mage.mana}")

    fireball = Fireball()
    icelance = IceLance()
    lightning = LightningBolt()

    mage.add_spell(fireball)
    mage.add_spell(icelance)
    mage.add_spell(lightning)

    print(f"Магу добавлены: {[s.name for s in mage.spells]}")

    print(f"Мана до: {mage.mana}")
    print(f"Огненный шар: урон={mage.cast_spell(0)}, мана={mage.mana}")
    print(f"Ледяное копьё: урон={mage.cast_spell(1)}, мана={mage.mana}")
    print(f"Молния: урон={mage.cast_spell(2)}, мана={mage.mana}")
    print(f"Молния (нет маны): урон={mage.cast_spell(2)}")