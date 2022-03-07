from builder import VehicleAbstractBuilder


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> VehicleAbstractBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: VehicleAbstractBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_default_vehicle(self) -> None:
        self.builder.produce_tire()
        self.builder.produce_boxes()
        self.builder.produce_tire()
