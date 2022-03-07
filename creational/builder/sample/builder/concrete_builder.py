from .abstract_builder import VehicleAbstractBuilder
from products import VehicleProduct


class VehicleBuilder(VehicleAbstractBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    _product: VehicleProduct = None

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = VehicleProduct()

    @property
    def product(self) -> VehicleProduct:
        product: VehicleProduct = self._product
        self.reset()
        return product

    def produce_boxes(self) -> None:
        self._product.add_new_part('boxes')

    def produce_fan(self) -> None:
        self._product.add_new_part('fan')

    def produce_umbrella(self) -> None:
        self._product.add_new_part('umbrella')

    def produce_tire(self) -> None:
        self._product.add_new_part('tire')
