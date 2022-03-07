from director import Director
from builder import VehicleBuilder


"""
In this case we are going to use a know game called Bad Piggies (from the angry birds sega). You can see the trailer
in next link https://www.youtube.com/watch?v=YsCpDaSooWA

In this game you must build a vehicle to cross an obstacles course with a limit parts like tire, boxes, umbrellas and
so on. we only focus in a build car under the following premises.
- There aren't limit of parts.
- I can build a vehicle by default.
- The user client can create a custom vehicle.
- We only mind the parts but not the position of them.
"""


def client_code():
    """
    The client can use a director class to create a prefab object, but also it can create a new object step to step
    only using a builder class. When the client has finished creating the vehicle call to 'builder.product' to get de
    vehicle, and we can see the parts using 'show_parts()' method.
    """
    director = Director()
    builder = VehicleBuilder()
    director.builder = builder

    print("Default vehicle: ")
    director.build_default_vehicle()
    print(builder.product.show_parts())

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom vehicle: ")
    builder.produce_tire()
    builder.produce_boxes()
    builder.produce_boxes()
    builder.produce_fan()
    builder.produce_umbrella()
    builder.produce_umbrella()
    print(builder.product.show_parts())


if __name__ == "__main__":
    client_code()


"""
Try it!
I have a challenge for you, I need a minimal functional vehicle, this vehicle only need a box and a tire for to running
and I also need a optimal vehicle that use every parts.
How could you implement them?
"""