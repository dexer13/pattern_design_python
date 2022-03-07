from abc import ABC, abstractmethod


class VehicleAbstractBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Vehicle objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_tire(self) -> None:
        pass

    @abstractmethod
    def produce_boxes(self) -> None:
        pass

    @abstractmethod
    def produce_umbrella(self) -> None:
        pass

    @abstractmethod
    def produce_fan(self) -> None:
        pass
