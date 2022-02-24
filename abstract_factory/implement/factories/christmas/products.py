from products import (
    AbstractPiranhaPlant,
    AbstractGoomba,
    AbstractPenguin
)


class ChristmasPiranhaPlant(AbstractPiranhaPlant):
    def draw(self) -> str:
        return "Draw a tape with a ornament"


class ChristmasGoomba(AbstractGoomba):
    def draw(self) -> str:
        return "Draw a christmas hat"


class ChristmasPenguin(AbstractPenguin):
    def draw(self) -> str:
        return "Draw a white mustache and a christmas hat"
