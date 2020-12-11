from typing import Tuple

import numpy as numpy

graphicDataType = numpy.dtype([("ch", numpy.int32), ("fg", "3B"), ("bg", "3B")])

tileDataType = numpy.dtype([("walkable", numpy.bool), ("transparent", numpy.bool), ("dark", graphicDataType), ("light", graphicDataType)])

def defineTile(*, walkable: int, transparent: int, dark: Tuple[int, Tuple[int, int, int]], light:Tuple[int, Tuple[int, int, int]]) -> numpy.ndarray:
    return numpy.array((walkable, transparent, dark, light), dtype=tileDataType)

floor = defineTile(walkable = True, transparent = True, dark = (ord(" "), (255, 255, 255), (50, 50, 150)), light = (ord(" "), (255, 255, 255), (200, 180, 50)))
wall = defineTile(walkable = False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100)), light = (ord(" "), (255, 255, 255), (130, 110, 50)))





