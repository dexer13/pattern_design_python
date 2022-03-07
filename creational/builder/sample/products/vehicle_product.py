from typing import Any


class VehicleProduct:
    parts: list = None

    def __init__(self):
        self.parts = list()

    def add_new_part(self, part: Any):
        self.parts.append(part)

    def show_parts(self):
        return self.parts
