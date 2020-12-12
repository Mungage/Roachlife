# We want to procedurally generate a dungeon map.
# What do we need to do?

# We basically want to create a game map object and fill it with different tiles depending on the algorithms we utilize.
# In order to do this we can create different objects representing these tiles. The "room" object.
# These objects can then be painted ontop of out GameMap

# Pseudocode
#1. We want to paint room objects randomly onto the map     -> the room needs to be defined in terms of tiles
#2. We want to draw connections between these room objects.
#3. We want to spawn enemies randomly within these rooms.

# We want the room to be defined in terms of starting coordinates x and y. And then the finished coordinates creating the 2D graph on the tilemap
# We need a way to paint this room to the map.

from typing import Set, Iterable, Iterator
from gameMap import GameMap
from entity import Entity
import tileTypes

import numpy

class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

def spawnEntities(self):
    raise NotImplementedError

def generate_connections(self):
    raise NotImplementedError

def generate_game_map(map_width: int, map_height: int, number_of_rooms: int, number_of_enemies: int, entities: Iterable[Entity]) -> GameMap:
# We want to draw a single room to the map
# In order to do this we want to let the map hold a room
# the rooms have a set of coordinates. So how do we update the 2D array in the GameMap with those?
# By accessing the 2D numpy array of tiles and adding the tiles
   
    number_of_rooms = number_of_rooms
    enemies = number_of_enemies

    room = Room(40, 50, 10, 5)

    gameMap = GameMap(width=map_width, height=map_height, entities=entities)
    
    gameMap.tiles[room.x1, 5] = tileTypes.wall

    return gameMap



