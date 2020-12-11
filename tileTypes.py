from typing import Tuple

import numpy as numpy

# This line
graphicDataType = numpy.dtype([("ch", numpy.int32), ("fg", "3B"), ("bg", "3B")])

tileDataType = numpy.dtype([("walkable", numpy.bool), ("transparent", numpy.bool), ("dark", graphicDataType)])

def defineTileType(*, walkable: int, transparent: int, dark: Tuple[int, Tuple[int, int, int]]) -> numpy.ndarray:
    """This function allows us to define more types of tiles for use in the game"""
    return numpy.array((walkable, transparent, dark), dtype=tileDataType)

# Defined tiles available for use by the game map
floor = defineTileType(walkable = True, transparent = True, dark = (ord(" "), (255, 255, 255), (50, 50, 150)),)
wall = defineTileType(walkable = False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100)),)





