from typing import Set, Iterable, Iterator, Tuple, List
from gameMap import GameMap
from entity import Entity
import tileTypes

import random

import numpy

class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    # We want to decide the room's area, which is defined as a 2D array i.e. the two slices x1:x2 and y1:y2
    def determine_room_size(self) -> Tuple[slice, slice]:
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

def spawn_Entities(self):
    raise NotImplementedError

def generate_connections(self):
    raise NotImplementedError

def generate_game_map(map_width: int, map_height: int, min_rooms, max_rooms: int, min_room_size: int, max_room_size: int,  max_enemies: int, entities: Iterable[Entity]) -> GameMap:
    # We want to make a room spawn randomly on the map
    # Random returns random integer in range [a, b] including both end points.
    # This means we should be able to use it to make the room spawn at a random spot on the map
    # Thus: use randint to get random x and y coordinates, then spawn the room using those.
    # Make the room a random width and height
    # Thus we need a randomized number between the coordinates 0,0 and the maximum width and maximum height supplied in the method.
    # We also need a rancomized number of rooms between a minimum and a maximum
    max_rooms = max_rooms
    max_enemies = max_enemies
    
    game_map = GameMap(width=map_width, height=map_height, entities=entities)
    number_of_rooms = random.randint(min_rooms, max_rooms)
    
    rooms: List[Room] = []

    i = 0
    while i < number_of_rooms:
        # Pick the coordinates to place the room
        x_start = random.randint(0, map_width)
        y_start = random.randint(0, map_height)
        # Pick the x and y size for the room
        x_size = random.randint(min_room_size, max_room_size)
        y_size = random.randint(min_room_size, max_room_size)
        # Add a new instance with the randomized integers
        new_room = Room(x_start, y_start, x_size, y_size)

        rooms.append(new_room)
        
        i += 1

    for room in rooms:
        game_map.tiles[room.determine_room_size()] = tileTypes.floor

    return game_map



