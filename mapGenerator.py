from __future__ import annotations  # Does something with the way the code is interpreted, solved a NameError

from typing import Set, Iterable, Iterator, Tuple, List
from gameMap import GameMap
from entity import Entity
import tileTypes

import random

class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    # We want to decide the room's area, which is defined as a 2D array i.e. the two slices x1:x2 and y1:y2
    @property
    def determine_room_size(self) -> Tuple[slice, slice]:
        return slice(self.x1 + 1, self.x2 + 1), slice(self.y1 + 1, self.y2)

    @property
    def determine_room_center(self) -> Tuple[int, int]:
        # We want to get the center coordinate of the room
        # We do this by dividing the full room by 2, we need to return a coordinate x and y.
        # This can be done as a Tuple I presume.
        return (self.x1 + self.x2 / 2), (self.y1 + self.y2 / 2)
    
    def check_room_collisions(self, old_room: Room) -> bool:
        # if rooms outer x1, x2 and y1, y2 intersects with another room, return true
        if  (self.x1 <= old_room.x2 and self.x2 >= old_room.x1 and self.y1 <= old_room.y2 and self.y2 >= old_room.y1):
            return True
          

def spawn_entities(entities: Iterable[Entity], player: Entity) -> None:
    # While max_enemies has not been reached
    # Call this function to spawn enemies
    # Also spawn the player
    # How do they get spawned?
    # Just by getting added to the entities list I presume?
    player.x = 50
    player.y = 50
    

def generate_connections(self):
    raise NotImplementedError

def generate_game_map(map_width: int, map_height: int, min_rooms, max_rooms: int, min_room_size: int, max_room_size: int,  max_enemies: int, entities: Iterable[Entity], player: Entity) -> GameMap:
    game_map = GameMap(width=map_width, height=map_height, entities=entities)
    
    number_of_rooms = random.randint(min_rooms, max_rooms)

    list_of_rooms: List[Room] = []

    i = 0
    while i < number_of_rooms:
        # Pick the coordinates to place the room
        x_start = random.randint(0, map_width - 1)
        y_start = random.randint(0, map_height - 1)
        # Pick the x and y size for the room
        x_size = random.randint(min_room_size, max_room_size)   
        y_size = random.randint(min_room_size, max_room_size)
        # Add a new instance with the randomized integers
        new_room = Room(x_start, y_start, x_size, y_size)

        # We want to check whether the list rooms has rooms that overlap with the new room before adding it to the list.
        # We do this by checking the new room against every room in the list. This requires a loop

        if any(new_room.check_room_collisions(room) for room in list_of_rooms):
            continue
            
        game_map.tiles[new_room.determine_room_size] = tileTypes.floor
        list_of_rooms.append(new_room)
        i += 1



    # We've got the rooms generated in the loop and appended to the list.
    # If room x overlaps with room y in list of rooms. Repeat the loop
    spawn_entities(entities, player)

    return game_map



