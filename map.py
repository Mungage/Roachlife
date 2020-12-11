
from typing import Iterable, Iterator
import numpy # numpy 

from entity import Entity
from tcod.console import Console

class Map:
    """This class is the actual map where the game is played out"""
    # The map need



    def __init__(self, engine: Engine, width: int, height: int, listOfEntities: Iterable[Entity]):
        self.width = width
        self.height = height
        self.listOfEntities = listOfEntities

        self.tiles = numpy.full((width, height), fill_value = tiles.wall, order = "F")
        self.visible = numpy.full((width, height), fill_value = False, order = "F") 

    def renderMap(self, console: Console) -> None:

        console.tiles_rgb[0 : self.width, 0 : self.height] = numpy.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
        )

        listOfSortedEntities = sorted( self.listOfEntities, key=lambda x: x.render)




