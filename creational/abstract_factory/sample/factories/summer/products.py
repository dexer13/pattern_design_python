from products import (
    AbstractPiranhaPlant,
    AbstractGoomba,
    AbstractPenguin
)


class SummerPiranhaPlant(AbstractPiranhaPlant):
    def draw(self) -> str:
        return "Draw a sunglasses"


class SummerGoomba(AbstractGoomba):
    def draw(self) -> str:
        return "Draw a straw hat"


class SummerPenguin(AbstractPenguin):
    def draw(self) -> str:
        return "Draw a hawaiian shirt"
