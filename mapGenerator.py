from typing import Set, Iterable, Iterator, Tuple
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

    # We want to decide the room's area
    def get_room_area(self) -> Tuple[slice, slice]:
        



        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

def spawnEntities(self):
    raise NotImplementedError

def generate_connections(self):
    raise NotImplementedError

def generate_game_map(map_width: int, map_height: int, number_of_rooms: int, number_of_enemies: int, entities: Iterable[Entity]) -> GameMap:
    # We want to draw a single room on the game map
    # In order to do this we want to generate the room
    # We want to have an area that defines the inner area of the room
    # We then want to print each line inside said room.

    number_of_rooms = number_of_rooms
    enemies = number_of_enemies

    room = Room(x=5, y=20, width=30, height=30)
    gameMap = GameMap(width=map_width, height=map_height, entities=entities)

    gameMap.tiles[room.get_room_area()] = tileTypes.floor

    return gameMap



