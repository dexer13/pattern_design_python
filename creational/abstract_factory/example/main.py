from __future__ import annotations

from abstract_factory import RaceAbstractFactory
from factories import (
    SummerRaceFactory,
    ChristmasRaceFactory
)
from products import (
    AbstractPiranhaPlant,
    AbstractGoomba,
    AbstractPenguin
)

""" 
In this implementation example I'm going to use patter to generate or instantiate objects for a mario kart race.
- Problem
When I'm playing mario kart this game have different objects depending seasons or important event holiday by example 
christmas. Each object doesn't have different script else different aspect visual. When I want to add an object to 
scene I don't want select a specific object like summer object, I just only add an object 
and internally it knows what aspect put according to the season or event currently.
- Solution 
In this case we have some family class by example summer is a family and christmas is an another family, so we need a 
ABSTRACT FACTORY to create different family objects like a piranha plant, which for the summer family class this plant
will have a sun glasses but the christmas family class it'll have a tape with ornaments.

En esta ejemplo de implementación vamos a usar el patron para generar o instanciar objetos de una carrera de Mario Kart.
- Problema
Cuando estoy jugando Mario Kart este juego tiene diferentes objetos dependiendo de la estación del año o un evento
importante como por ejemplo la navidad. Cada objeto no tiene diferente comportamiento pero si diferente aspecto visual.
Cuando quiero agregar un objecto a la escena yo no quiero seleccionar un especifico objecto como por ejemplo un objeto 
de verano, Yo solo agregro un objeto e internamente el sistema sabe que aspecto en especifico poner de acuerdo a la 
temporada o evento actual.
- Solución
En este caso nosotros tenemos algunas clases de familias, por ejemplo, verano es una familia y navidad es otra familia,
Entonces necesitamos una FABRICA ASBTRACTA asbtracta para crear diferentes familias de objetos como una plata piraña, 
la cual para la clases de familia de verano esta planta tendrá unas gafas de sol mientras pero para las clases de 
familias de navidad esta tendra una cinta con adornos.
"""


def client_code(factory: RaceAbstractFactory) -> None:
    """
    This client doesn't know about the season or event, It just only knows about the objects that need to create

    Este cliente no conoce acerca de las estaciones o eventos, él solo sabe que necesita crear objetos.
    """
    piranha_plant: AbstractPiranhaPlant = factory.create_piranha_plant()
    goomba: AbstractGoomba = factory.create_goomba()
    penguin: AbstractPenguin = factory.create_penguin()
    print("draw piranha plan")
    print(f"{piranha_plant.draw()}")
    print("draw goomba")
    print(f"{goomba.draw()}")
    print("died goomba")
    print(f"{goomba.died()}")
    print("draw penguin")
    print(f"{penguin.draw()}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Set a summer family")
    client_code(SummerRaceFactory())

    print("\n")

    print("Set a christmas family")
    client_code(ChristmasRaceFactory())


"""
Try it!
Right now you know the problem and how the ABSTRACT FACTORY pattern working, you should try it:
- Add a new family class called "Halloween" and create objects like you see above

Intentalo!
Ahora que tu conoces el problema y como el patron de FABRICA ABSTRACTA funciona, tu deberias intentar lo siguiente:
- Agrega una nueva clases de familias llamadas "Halloween" y crea objetos tal y como vez en la parte superior 
"""
