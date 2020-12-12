from typing import Tuple

import numpy as numpy

# This line is meant to create a data type by using the dtype function from the numpy package.
# The data type itself is similar to a struct and is compatible with the tcod cConsole.tiles_rgb function
graphicDataType = numpy.dtype(
    [
        ("ch", numpy.int32),   # The Unicode codepoint, i.e. the character represented in integer format.
        ("fg", "3B"),   # The foreground color, i.e. the text that gets rendered on the console.
        ("bg", "3B")    # The background color, i.e. the tiles that get rendered on the console.
        # 3B means 3 unsigned bytes, which can be uised for RGB color codes.
    ]
)
# A tile can be a different unicode character, can have a fdifferent 

# This line is the data type that holds our statically defined tile data. I.e. the actual properties of the tile.
# Whether it is walkable, transparent, dark, light etc.
tileDataType = numpy.dtype(
    [
        ("walkable", numpy.bool),       # A tile can be walkable, either yes or no.
        ("transparent", numpy.bool),    # A tile can be transparent
        ("dark", graphicDataType)       # A tile can be dark/light etc.
    ]
)
# In conclusion: Both of these data types represent the data structure for the tiles that we will use. 
# The first one represents the graphics of a tile, 
# While the second one represents the actual tile and its properties.
# the "dark" property in turn utilizes the graphicDataType we defined earlier. I.e. the graphics to be used while the tile is "dark"

# We use this function to define our different tyle types, quite similarly to how we define entities in the entity factory.
# The function takes the parameters that correspond to the possible elemnts within the data structs we created above.
def defineTileType( 
    *,                                          # This means input order doesn't matter, but enforces keyword usage
    walkable: bool,                             # We insert whether the tile we're defining should be walkable
    transparent: bool,                          # If it should be transparent
    dark: Tuple[int, Tuple[int, int, int]]      # And what color it should be. "dark" refers
    ) -> numpy.ndarray:                         # We return the defined tile as a numpy array.
    """This function allows us to define more types of tiles for use in the game"""
    return numpy.array((walkable, transparent, dark), dtype=tileDataType)   # Onced defined we return the tile as a tileDataType.

# Defined tiles available for use by the game map
floor = defineTileType(
    walkable = True, 
    transparent = True, 
    dark = (ord(" "), (255, 255, 255), (50, 50, 150)),   
    )

# This is the finished, defined tile that we can utilize. the "dark" property is defined by the graphicsDataType we defined before.
# In this case we use ord(" ") to retrieve the unicode character we want to use, and then the rgb colors used by the foreground and background
# Represented by the three unsigned bytes each.
wall = defineTileType(walkable = False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100)),)





