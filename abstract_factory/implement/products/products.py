from abc import ABC, abstractmethod


class AbstractPiranhaPlant(ABC):

    @abstractmethod
    def draw(self) -> str:
        pass


class AbstractGoomba(ABC):

    @abstractmethod
    def draw(self) -> str:
        pass

    def died(self) -> str:
        return 'I am died'


class AbstractPenguin(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass
