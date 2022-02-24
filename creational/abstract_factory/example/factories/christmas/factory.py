from abstract_factory import RaceAbstractFactory
from products import (
    AbstractPiranhaPlant,
    AbstractGoomba,
    AbstractPenguin
)
from .products import (
    ChristmasGoomba,
    ChristmasPenguin,
    ChristmasPiranhaPlant
)


class ChristmasRaceFactory(RaceAbstractFactory):
    """
    Concrete summer produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_piranha_plant(self) -> AbstractPiranhaPlant:
        return ChristmasPiranhaPlant()

    def create_goomba(self) -> AbstractGoomba:
        return ChristmasGoomba()

    def create_penguin(self) -> AbstractPenguin:
        return ChristmasPenguin()
