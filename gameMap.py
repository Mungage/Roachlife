from __future__ import annotations

import numpy # numpy 

from tcod.console import Console

from typing import Iterable, Optional, TYPE_CHECKING

import tileTypes

if TYPE_CHECKING:
    from entity import Entity

class GameMap:
    """The purpose of the map is to represent the actual map where the player can move and interact with other entities.
    The map object is initialized by the main() function.
    The responsibility of the map is to hold and display the tiles"""

    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):    # We initialize the map file
        self.width = width      # It takes in a width in tiles
        self.height = height    # And a height in tiles
        self.entities = set(entities)
                                            
        # We use numpy array and then fill it with the appropriate tiles from the tiles file.
        # This variable is the actual representation of the tiles on the map, and are expressed as a 2D numpyarray.
        self.tiles = numpy.full((width, height), fill_value = tileTypes.wall, order = "F")     

        # We set the map's tiles at coordinates x and y to be of a tileType walls   
        # The tiles are an ndarray because we formatted it as such with numpy before.                                                   

    def inside_boudaries(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height # True if the x and y coordinates are inside of the map's boundaries.

    # This function renders the map within our established console context. The console.tiles_rgb quickly renders the entire map for us.
    # This function is much quicker than the console.print that we use to render the entities.
    def render_map(self, console: Console) -> None:

        # The tiles_rgb function from tcod quickly renders the whole map using the assigned tiles
        # In other words it takes the widght and height we used when initializing the map. It then renders everything much more
        # efficiently than the console.print function.
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]

        for entity in self.entities:
           console.print(entity.x, entity.y, entity.charTile, fg=entity.color) # The print function is not as efficient as tiles_rgb, but can be used to render entities.
        
        
    # We use this function to ensure that the player can't move beyond the map into the void.









