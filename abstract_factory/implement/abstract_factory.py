from abc import ABC, abstractmethod

from products import (
    AbstractPiranhaPlant,
    AbstractGoomba,
    AbstractPenguin
)


class RaceAbstractFactory(ABC):
    """
    The Abstract Factory interface.
    """
    @abstractmethod
    def create_piranha_plant(self) -> AbstractPiranhaPlant:
        pass

    @abstractmethod
    def create_goomba(self) -> AbstractGoomba:
        pass

    @abstractmethod
    def create_penguin(self) -> AbstractPenguin:
        pass


