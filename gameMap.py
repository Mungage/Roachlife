
from typing import Iterable, Iterator
import numpy # numpy 

import tileTypes

from tcod.console import Console
class GameMap:
    """The purpose of the map is to represent the actual map where the player can move and interact with other entities.
    The map object is initialized by the main() function.
    The responsibility of the map is to hold and display the tiles"""

    def __init__(self, width: int, height: int):    # We initialize the map file
        self.width = width      # It needs a width in tiles
        self.height = height    # And a height in tiles
                                           
        # We use numpy array and then fill it with the appropriate tiles from the tiles file.
        # This variable is the actual representation of the tiles on the map, and are expressed as a 2D numpyarray.
        self.tiles = numpy.full((width, height), fill_value = tileTypes.floor, order = "F")     

        # We set the map's tiles at coordinates x and y to be of a tileType walls   
        # The tiles are an ndarray because we formatted it as such with numpy before.                                                   
        self.tiles[30:33, 22] = tileTypes.wall

    # This function renders the map within our established console context. The console.tiles_rgb quickly renders the entire map for us.
    # This function is much quicker than the console.print that we use to render the entities.
    def renderMap(self, console: Console) -> None:
       console.tiles_rgb[0 : self.width, 0 : self.height] = self.tiles["dark"]

    # This function checks whether 
    def insideBoudaries(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height # True if the x and y coordinates are inside of the map's boundaries.





